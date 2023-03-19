import logging
from cache.redis_wrapper import RedisModel

class GuestModel(RedisModel):
  guest = None

  def __init__(self):
    super().__init__(
      description_cells=(('A', 7), ('K', 7)),
      value_cells=(('A', 8), ('K', 82))
    )

  @classmethod
  def getGuests(cls):
    if cls.guest is None:
      cls.guest = GuestModel()
    return cls.guest

  @classmethod
  def find_by_id(cls, id):
    guest = GuestModel()
    for guest in guest.rows:
      if guest.id == id:
        return guest
