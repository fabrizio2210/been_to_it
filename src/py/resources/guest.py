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
  parser.add_argument('alergie',
                      type=str,
                      help="If there are some allergens ."
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
      if data.get('alergie') is not None:
        guest.alergie = data.get('alergie')
      if data.get('note') is not None:
        guest.note = data.get('note')
    else:
      return {'message': 'Item not found.'}, 404
    return {'guest': guest.json(exclude=Guest.exclude_on_its_own)}, 201

class GuestList(Resource):
  def get(self):
    return {'guests': list(map(lambda x: x.json(include=Guest.include_for_others),
                           GuestModel.get_all_guests()))
           }


