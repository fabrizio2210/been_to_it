import inspect
import logging
import os
import time
from redis import Redis

def slowdown():
  if os.getenv('ENVIRONMENT', None) == 'DEV':
    time.sleep(0.005)

class RedisWrapper():
  client = None
  memoization = {}

  @classmethod
  def init(cls, url):
    cls.client = Redis.from_url(url)

  @classmethod
  def publish(cls, msg):
    cls.client.publish('sse', msg)

  @classmethod
  def write(cls, cell, value):
    logging.debug('Writing (%s,%d) to Redis' % cell)
    cls.client.hset('write_hash', key='%s%d' % cell, value=value)
    slowdown()

  @classmethod
  def reassemblyValue(cls, values):
    if values[0] is not None:
      logging.debug('Value "%s" read from write_hash.', values[0])
      return values[0].decode('utf-8')
    elif values[1] is not None:
      return values[1].decode('utf-8')

  @classmethod
  def commandToWriteCache(cls, pipe, cell, value):
    logging.debug('Writing (%s,%d) to Redis cache' % cell)
    pipe.set('%s%d' % cell, value=value)

  @classmethod
  def readCacheToWrite(cls):
    cache_to_write = {}
    for keyvalues in cls.client.hscan_iter('write_hash'):
      cache_to_write[keyvalues[0].decode('utf-8')] = keyvalues[1].decode('utf-8')
    return cache_to_write

  @classmethod
  def commandToRead(cls, pipe, cell):
    pipe.hget('write_hash', key='%s%d' % cell)
    pipe.get('%s%d' % cell)

  @classmethod
  def read(cls, cell, memoize=False):
    if memoize:
      value = cls.memoization.get(cell, None)
      if value is not None:
        return value

    logging.debug('Reading (%s,%d) from Redis' % cell)
    pipe = cls.client.pipeline()
    cls.commandToRead(pipe, cell)
    values = pipe.execute()
    slowdown()
    value = cls.reassemblyValue(values)

    if memoize:
      cls.memoization[cell] = value
    return value

  @classmethod
  def enque_photo(cls, photo_pb):
    cls.client.lpush('in_photos', photo_pb.SerializeToString())


class RedisRow():

  def __init__(self, fn_dict, attrs):
    logging.debug("Setting fn_dict:%s", fn_dict)
    self._fn_dict = fn_dict
    self._attrs = attrs

  def __getattr__(self, name: str):
    value = self.__dict__.get(f"{name}", None)
    if value is None:
      value = self.__dict__.get('_fn_dict', None)
      if value is not None:
        value = self.__dict__['_fn_dict'][f"{name}_get"]()
    return value

  def __setattr__(self, name, value):
    if name in ['_fn_dict', '_attrs']:
      self.__dict__[f"{name}"] = value
    else:
      self.__dict__['_fn_dict'][f"{name}_set"](value)

  def json(self, exclude=[], include=None, ppipe=None):
    pipe = ppipe
    if ppipe is None:
      pipe = RedisWrapper.client.pipeline()

    keys = []
    for attr in sorted(self._attrs):
      logging.debug("attr: %s", attr)
      if attr.startswith('_'):
        continue
      if attr in exclude:
        continue
      if include is not None and attr not in include:
        continue
      RedisWrapper.commandToRead(pipe, self._attrs[attr])
      keys.append(attr)

    if ppipe is None:
      values = pipe.execute()
      slowdown()

      json = {}
      i = 0
      for attr in sorted(self._attrs):
        logging.debug("attr: %s", attr)
        if attr.startswith('_'):
          continue
        if attr in exclude:
          continue
        if include is not None and attr not in include:
          continue
        logging.debug("Values: %s", values[i:i+2])
        json[attr] = RedisWrapper.reassemblyValue(values[i:i+2])
        i += 2
      return json
    return keys


class RedisModel():

  def __init__(self, description_cells, value_cells):
    self.rows = {}
    value_columns_length = len(list(RedisModel.expand_cols(value_cells)))
    description_columns_length = len(
      list(RedisModel.expand_cols(description_cells))
    )
    if value_columns_length != description_columns_length:
      raise ValueError(
        'Columns of description cells (%d) differ from columns of value cells (%d)'
        % (description_columns_length, value_columns_length)
      )
    index = 0
    for row in RedisModel.expand_rows(value_cells):
      fn_dict = {}
      attrs = {} 
      offset = 0
      id_key = ""
      for col in RedisModel.expand_cols(value_cells):
        def get_fn(col=col, row=row):
          return RedisWrapper.read((col, row))

        def set_fn(value, col=col, row=row):
          RedisWrapper.write((col, row), value)

        desc = RedisWrapper.read(
            (chr(ord(description_cells[0][0]) + offset), description_cells[0][1]),
            memoize=True
          ) 
        if desc is not None:
          logging.debug("Set \"%s\" as attr for \"%s\"", desc.lower(), row)
          fn_dict["%s_get" % desc.lower()]=get_fn
          fn_dict["%s_set" % desc.lower()]=set_fn
          attrs[desc.lower()] = (col, row)
          if desc.lower() == "id":
            id_key = get_fn()
        offset += 1
      if len(fn_dict) > 0:
        if id_key == "":
          id_key = index
        self.rows[id_key]=RedisRow(fn_dict, attrs)
        index += 1

  def __repr__(self):
    out = "Rows:\n"
    for row in self.rows:
      out += str(rows[row]._fn_dict)
    return out
  
  @classmethod
  def expand_cols(cls, cells_range):
    start_col = cells_range[0][0]
    end_col = cells_range[-1][0]
    for col in range(ord(start_col), ord(end_col)+1):
      yield chr(col)
      
  @classmethod
  def expand_rows(cls, cells_range):
    start_row = cells_range[0][1]
    end_row = cells_range[-1][1]
    for row in range(start_row, int(end_row)+1):
      yield row 

