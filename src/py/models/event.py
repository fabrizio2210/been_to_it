import logging
from cache.redis_wrapper import RedisModel


class EventModel(RedisModel):
  description_cell = ('A', 1)
  value_cell = ('A', 2)
  
  def __init__(self):
    #super().__init__(
    #  description_cells=(EventModel.description_cell,),
    #  value_cells=(EventModel.value_cell,)
    #  )
    pass

  def json(self):
    return {
        'descrizione_par1': self.descrizione_par1,
        'descrizione_par2': self.descrizione_par2,
        'descrizione_par3': self.descrizione_par3,
      }

