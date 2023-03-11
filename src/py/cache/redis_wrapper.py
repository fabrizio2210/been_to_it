import logging
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
    logging.debug('Reading (%s,%d) from Redis'% cell)
    # check cache TTL
    if time.now() - cls.client.get('last_sync_read') > 60:
      Sheet.read_sync()
    # read from redis if available
    # otherwise read from sheet all the data (not just the cell)
    # update cache TTL

  @classmethod
  def enque_photo(cls, photo_pb):
    cls.client.lpush('in_photos', photo_pb.SerializeToString())


class RedisRow():
  pass
    

class RedisModel():
  rows = []

  def __init__(self, description_cells, value_cells):
    value_columns_length = len(RedisModel.expand_cols(value_cells))
    description_columns_length = len(RedisModel.expand(description_cells))
    if value_columns_length != description_columns_length:
      logging.error(
        'Columns of description cells (%d) differ from colums of value cells (%d)' %
        (description_columns_length, value_columns_length))
      raise ValueError('Description colums mismatch with value columns.')
    for row in RedisModel.expand_rows(value_cells):
      row_obj = RedisRow()
      offset = 0
      for col in RedisModel.expand_cols(value_cells):
        def get_fn(self, col=col, row=row):
          return RedisWrapper.read((col, row))

        def set_fn(self, value, col=col, row=row):
          RedisWrapper.write((col, row), value)

        desc = RedisWrapper.read(
            (char(ord(description_cells[0][0]) + offset), description_cells[0][1])
          ) 
        setattr(row_obj, desc, property(get_fn, set_fn)) 
        offset += 1
      rows.append(row_obj)
  
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
    for row in range(start_row, end_row+1):
      yield row 
