import io
import werkzeug
import logging
from flask_restful import Resource, reqparse
from models.guest import GuestModel


class Guest(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('presence',
                      type=str,
                      required=True,
                      help="Presence to the event."
                      )

  def get(self, id):
    id = str(id)
    guest = GuestModel.find_by_id(id)
    if guest:
      return {'guest': guest.json()}, 200
    return {'message': 'Item not found.'}, 404

  def put(self, id):
    id = str(id)
    if os.getenv('BLOCK_UPLOAD', False):
      return { 'message':
        os.getenv('BLOCK_UPLOAD_MSG', 'The upload is blocked by admin.')}, 403
    data = Photo.parser.parse_args()
    photo = PhotoModel.find_by_id(id)
    if photo:
      if photo[0].author_id == data.get('author_id', None):
        if data.get('description') is not None:
          photo[0].description = data.get('description')
        if data.get('author') is not None:
          photo[0].author = data.get('author')
        photo[0].save_to_db()
        # Notify other clients
        #RedisWrapper.publish('changed ' + str(photo[0].id))
      else:
        return {'message': 'Not authorized'}, 403
    else:
      return {'message': 'Item not found.'}, 404
    return {'photo': FileManager.photo_to_client(photo[0].json())}, 201

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


