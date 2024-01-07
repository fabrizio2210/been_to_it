import logging
from cache.redis_wrapper import RedisModel


class EventModel(RedisModel):
  event = None
  
  def __init__(self):
    super().__init__(
      tab='Evento',
      description_cells=(('A', 1), ('K', '1')),
      value_cells=(('A', 2), ('K', '3'))
      )

  @classmethod
  def getEvent(cls):
    if cls.event is None:
      cls.event = EventModel()
    elif len(cls.event.rows) == 0:
      cls.event = EventModel()
    return cls.event

