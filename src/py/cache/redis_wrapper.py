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
    cls.client.set('%s%d' % cell, value)
    slowdown()
    cls.client.hset('write_hash', key='%s%d' % cell, value=value)
    slowdown()

  @classmethod
  def read(cls, cell, memoize=False):
    if memoize:
      value = cls.memoization.get(cell, None)
      if value is not None:
        return value

    logging.debug('Reading (%s,%d) from Redis' % cell)
    pipe = cls.client.pipeline()
    pipe.hget('write_hash', key='%s%d' % cell)
    pipe.get('%s%d' % cell)
    values = pipe.execute()
    slowdown()
    if values[0] is not None:
      value = values[0]
      logging.debug('Value "%s" read from write_hash.', value)
    else:
      value = values[1]

    if value is not None:
      value = value.decode('utf-8')
      if memoize:
        cls.memoization[cell] = value
      return value
    return None

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

  def json(self, exclude=[], include=None):
    json = {}
    for attr in self._attrs:
      logging.debug("attr: %s", attr)
      if attr.startswith('_'):
        continue
      if attr in exclude:
        continue
      if include is not None and attr not in include:
        continue
      json[attr] = getattr(self, attr)
    return json


class RedisModel():

  def __init__(self, description_cells, value_cells):
    self.rows = []
    value_columns_length = len(list(RedisModel.expand_cols(value_cells)))
    description_columns_length = len(
      list(RedisModel.expand_cols(description_cells))
    )
    if value_columns_length != description_columns_length:
      raise ValueError(
        'Columns of description cells (%d) differ from columns of value cells (%d)'
        % (description_columns_length, value_columns_length)
      )
    for row in RedisModel.expand_rows(value_cells):
      fn_dict = {}
      attrs = []
      offset = 0
      for col in RedisModel.expand_cols(value_cells):
        def get_fn(col=col, row=row):
          return RedisWrapper.read((col, row))

        def set_fn(value, col=col, row=row):
          RedisWrapper.write((col, row), value)

        desc = RedisWrapper.read(
            (chr(ord(description_cells[0][0]) + offset), description_cells[0][1]),
            memoize=True
          ) 
        logging.debug("Set \"%s\" as attr for \"%s\"", desc.lower(), row)
        fn_dict["%s_get" % desc.lower()]=get_fn
        fn_dict["%s_set" % desc.lower()]=set_fn
        attrs.append(desc.lower())
        offset += 1
      self.rows.append(RedisRow(fn_dict, attrs))

  def __repr__(self):
    out = "Rows:\n"
    for row in self.rows:
      out += str(row._fn_dict)
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

