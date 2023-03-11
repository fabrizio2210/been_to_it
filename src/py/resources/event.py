import os
import werkzeug
import logging
from flask_restful import Resource, reqparse
from cache.redis_wrapper import RedisWrapper


class Event(Resource):

  def get(self):
    event = RedisWrapper.get_event()
    if event:
      return {'event': event.json()}, 200
    return {'message': 'Item not found.'}, 404

