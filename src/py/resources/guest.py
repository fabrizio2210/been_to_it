import io
import werkzeug
import logging
from flask_restful import Resource, reqparse
from models.guest import GuestModel


class Guest(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('viene',
                      type=str,
                      help="Presence to the event."
                      )
  parser.add_argument('stanza',
                      type=str,
                      help="If a room is needed."
                      )
  parser.add_argument('allergie',
                      type=str,
                      help="If there are some allergens ."
                      )
  parser.add_argument('pulmino',
                      type=str,
                      help="If a shuttle is needed."
                      )
  parser.add_argument('email',
                      type=str,
                      help="Their email."
                      )
  parser.add_argument('note',
                      type=str,
                      help="A note about their presence."
                      )
  exclude_on_its_own = ['note_interne']
  include_for_others = ['nome', 'viene']

  def get(self, id):
    id = str(id)
    guest = GuestModel.find_by_id(id)
    if guest:
      return {'guest': guest.json(exclude=Guest.exclude_on_its_own)}, 200
    return {'message': 'Item not found.'}, 404

  def put(self, id):
    id = str(id)
    guest = GuestModel.find_by_id(id)
    data = Guest.parser.parse_args()
    logging.debug("data=%s", data)
    if guest:
      if data.get('viene') is not None:
        guest.viene = data.get('viene')
      if data.get('stanza') is not None:
        guest.stanza = data.get('stanza')
      if data.get('allergie') is not None:
        guest.allergie = data.get('allergie')
      if data.get('pulmino') is not None:
        guest.pulmino = data.get('pulmino')
      if data.get('email') is not None:
        guest.email = data.get('email')
      if data.get('note') is not None:
        guest.note = data.get('note')
    else:
      return {'message': 'Item not found.'}, 404
    return {'guest': guest.json(exclude=Guest.exclude_on_its_own)}, 201

class GuestList(Resource):
  def get(self, id):
    id = str(id)
    guest = GuestModel.find_by_id(id)
    if guest is not None:
      group = guest.gruppo
      json = []
      guests = GuestModel.get_all_guests()
      for guest in guests:
        if group == 'Torta':
          if guests[guest].gruppo == 'Torta':
            json.append(guests[guest].json(include=Guest.include_for_others))
        else:
          if guests[guest].gruppo != 'Torta':
            json.append(guests[guest].json(include=Guest.include_for_others))
      return {'guests': json}, 200
    return {'message': 'User ID not found.'}, 404


