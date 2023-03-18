import os
import werkzeug
import logging
from flask_restful import Resource, reqparse
from cache.redis_wrapper import RedisWrapper
from models.event import EventModel


class Event(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('uid',
                      type=str,
                      required=False,
                      help="User identifier."
                      )

  def get(self):
    data = Event.parser.parse_args()
    event = EventModel()

    if data.get('uid', None) in [
     "apre", "arti", "basa", "dava",
     "seri", "ieri", "noci", "melo",
     "nodi", "alti", "lima" ]:
      logging.debug("Event: %s", event)
      logging.debug("descrizione_torta: %s", event.rows[0].descrizione_torta_par1)
      event.descrizione_par1 = event.rows[0].descrizione_torta_par1
      event.descrizione_par2 = event.rows[0].descrizione_torta_par2
      event.descrizione_par3 = event.rows[0].descrizione_torta_par3
    return {'event': event.json()}, 200

