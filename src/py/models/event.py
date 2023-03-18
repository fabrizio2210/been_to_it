import logging
from cache.redis_wrapper import RedisModel


class EventModel(RedisModel):
  description_cells = (('A', 3), ('G', '3'))
  value_cells = (('A', 4), ('G', '4'))
  
  def __init__(self):
    super().__init__(
      description_cells=(EventModel.description_cells),
      value_cells=(EventModel.value_cells)
      )

  def json(self):
    return {
        'descrizione_par1': self.descrizione_par1,
        'descrizione_par2': self.descrizione_par2,
        'descrizione_par3': self.descrizione_par3,
      }

