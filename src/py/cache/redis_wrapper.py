import logging
import inspect
from redis import Redis

class RedisWrapper():
  client = None

  @classmethod
  def init(cls, url):
    cls.client = Redis.from_url(url)

  @classmethod
  def publish(cls, msg):
    cls.client.publish('sse', msg)

  @classmethod
  def write(cls, cell):
    pass

  @classmethod
  def read(cls, cell):
    logging.debug('Reading (%s,%d) from Redis' % cell)
    value = cls.client.get('%s%d' % cell)
    if value is not None:
      return value.decode('utf-8')
    return None

  @classmethod
  def enque_photo(cls, photo_pb):
    cls.client.lpush('in_photos', photo_pb.SerializeToString())


class RedisRow():
  _fn_dict = {}

  def __init__(self, fn_dict):
    self._fn_dict = fn_dict

  def __getattr__(self, name: str):
    value = self.__dict__.get(f"{name}", None)
    if value is None:
      value = self.__dict__.get('_fn_dict', None)
      if value is not None:
        value = self.__dict__['_fn_dict'][f"{name}_get"]()
    return value

  def __setattr__(self, name, value):
    if name != '_fn_dict':
      self.__dict__['_fn_dict'][f"{name}_set"](value)
    else:
      self.__dict__[f"{name}"] = value


class RedisModel():
  rows = []

  def __init__(self, description_cells, value_cells):
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
      offset = 0
      for col in RedisModel.expand_cols(value_cells):
        def get_fn(col=col, row=row):
          return RedisWrapper.read((col, row))

        def set_fn(value, col=col, row=row):
          RedisWrapper.write((col, row), value)

        desc = RedisWrapper.read(
            (chr(ord(description_cells[0][0]) + offset), description_cells[0][1])
          ) 
        logging.debug("Set \"%s\" as attr", desc.lower())
        fn_dict["%s_get" % desc.lower()]=get_fn
        fn_dict["%s_set" % desc.lower()]=set_fn
        offset += 1
      self.rows.append(RedisRow(fn_dict))

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
