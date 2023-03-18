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
  parser.add_argument('note',
                      type=str,
                      help="A note about their presence."
                      )

  def get(self, id):
    id = str(id)
    guest = GuestModel.find_by_id(id)
    if guest:
      return {'guest': guest.json()}, 200
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
      if data.get('note') is not None:
        guest.note = data.get('note')
    else:
      return {'message': 'Item not found.'}, 404
    return {'guest': guest.json()}, 201

class GuestList(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('timestamp',
                      type=int,
                      required=False,
                      help="If timestamp is provided, get latest photos after timestamp."
                      )
  parser.add_argument('author_id',
                      type=str,
                      required=False,
                      help="If author_id is provided, get all the photos of that author."
                      )
  def get(self):
    data = PhotoList.parser.parse_args()
    if data.get('author_id', None):
      return {'photos': list(map(lambda x:
                             FileManager.photo_to_client(x.json()),
                             PhotoModel.get_photos_by_author_id(data['author_id'])
                             ))
             }
    if data.get('timestamp', None):
      return {'photos': list(map(lambda x: 
                             FileManager.photo_to_client(x.json()),
                             PhotoModel.find_by_timestamp(data['timestamp'])
                         ))
             }
    logging.debug("In the resources: %s", PhotoModel.get_all_photos())
    return {'photos': list(map(lambda x: 
                           FileManager.photo_to_client(x.public_json()),
                           PhotoModel.get_all_photos()
                       ))
           }


