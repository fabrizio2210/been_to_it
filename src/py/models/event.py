import logging
from cache.redis_wrapper import RedisModel


class EventModel(RedisModel):
  event = None
  
  def __init__(self):
    super().__init__(
      description_cells=(('A', 3), ('G', '3')),
      value_cells=(('A', 4), ('G', '5'))
      )

  @classmethod
  def getEvent(cls):
    if cls.event is None:
      cls.event = EventModel()
    return cls.event

