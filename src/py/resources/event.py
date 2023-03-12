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
    # event = RedisWrapper.get_event()
    event = EventModel()

    if data.get('uid', None) in [
     "apre", "arti", "basa", "dava",
     "seri", "ieri", "noci", "melo",
     "nodi", "alti", "lima" ]:
      event.descrizione_par1 = "22 settembre dalle 21.00<br />Pinzonerkeller<br />P.za S. Stefano Montagna (BZ)"
      event.descrizione_par2 = "Taglio della torta<br /> festa fino a tarda sera"
      event.descrizione_par3 = "Per favore, conferma la tua<br />presenza tramite telefono<br />3471226481 o mail<br />fabrizio2210@gmail.com<br />"
    else:
      event.descrizione_par1 = "22 settembre dalle 15.00<br />Pinzonerkeller<br />P.za S. Stefano Montagna (BZ)"
      event.descrizione_par2 = "Seguirà cena in loco <br />fino a tarda sera"
      event.descrizione_par3 = "Per favore, conferma la tua<br />presenza tramite telefono<br />3471226481 o mail<br />fabrizio2210@gmail.com<br />"
    if event:
      return {'event': event.json()}, 200
    return {'message': 'Item not found.'}, 404

