import logging
from cache.redis_wrapper import RedisModel


class EventModel(RedisModel):
  description_cell=('A', 1)
  value_cell=('A', 2)
  
  def __init__(self):
    super(
      description_cells=(EventModel.description_cell,)
      value_cells=(EventModel.value_cell,)
      )

  def json(self):
    return {
        'description': self.rows[0].description,
      }

