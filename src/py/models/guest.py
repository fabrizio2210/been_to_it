import logging
from cache.redis_wrapper import RedisModel

class GuestModel(RedisModel):
  guest = None

  def __init__(self):
    super().__init__(
      tab='Invitati',
      description_cells=(('A', 3), ('L', 3)),
      value_cells=(('A', 4), ('L', 120))
    )

  @classmethod
  def getGuests(cls):
    if cls.guest is None:
      cls.guest = GuestModel()
    elif len(cls.guest.rows) == 0:
      cls.guest = GuestModel()
    return cls.guest

  @classmethod
  def find_by_id(cls, id):
    guests = GuestModel.getGuests()
    return guests.rows.get(id, None)

  @classmethod
  def get_all_guests(cls):
    guests = GuestModel.getGuests()
    return guests.rows
