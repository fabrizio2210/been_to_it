import logging
from cache.redis_wrapper import RedisModel


class EventModel(RedisModel):
  event = None
  
  def __init__(self):
    super().__init__(
      description_cells=(('A', 3), ('G', '3')),
      value_cells=(('A', 4), ('G', '4'))
      )

  def json(self):
    return {
        'descrizione_par1': self.descrizione_par1,
        'descrizione_par2': self.descrizione_par2,
        'descrizione_par3': self.descrizione_par3,
      }

  @classmethod
  def getEvent(cls):
    if cls.event is None:
      cls.event = EventModel()
    return cls.event
