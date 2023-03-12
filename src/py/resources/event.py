import os
import werkzeug
import logging
from flask_restful import Resource, reqparse
from cache.redis_wrapper import RedisWrapper
from models.event import EventModel


class Event(Resource):

  def get(self):
    # event = RedisWrapper.get_event()
    event = EventModel()
    event.descrizione_par1 = "22 settembre dalle 15.00<br />Pinzonerkeller<br />P.za S. Stefano Montagna (BZ)"
    event.descrizione_par2 = "Seguirà cena in loco <br />fino a tarda sera"
    event.descrizione_par3 = "Per favore, conferma la tua<br />presenza tramite telefono<br />3471226481 o mail<br />fabrizio2210@gmail.com<br />"
    if event:
      return {'event': event.json()}, 200
    return {'message': 'Item not found.'}, 404

