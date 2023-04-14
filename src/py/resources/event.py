import os
import werkzeug
import logging
from flask_restful import Resource, reqparse
from cache.redis_wrapper import RedisWrapper
from models.event import EventModel
from models.guest import GuestModel


class Event(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('uid',
                      type=str,
                      required=False,
                      help="User identifier."
                      )

  def get(self):
    data = Event.parser.parse_args()
    event = EventModel.getEvent()

    if data.get('uid', None):
      guest = GuestModel.find_by_id(data['uid'])
      if guest:
        if guest.gruppo.lower() == "torta":
          return {'event': event.rows["1"].json()}, 200
    evento = event.rows.get("0")
    if evento is None:
      return {}, 404
    return {'event': evento.json()}, 200

