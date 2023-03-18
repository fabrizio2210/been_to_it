from flask import Flask, Response
from flask_restful import Api
from flask_cors import CORS
from resources.event import Event
from resources.guest import Guest #, GuestList
import logging
import os

from cache.redis_wrapper import RedisWrapper
from utility.networking import get_my_ip

if __name__ == '__main__' or os.getenv('DEBUG', 0) == '1':
  logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Initiate Flask
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

# API
api.add_resource(Guest,       '/api/guest/<string:id>')
#api.add_resource(GuestList,   '/api/guests')
api.add_resource(Event,       '/api/event')

# Initialise from envrironment variables
RedisWrapper.init(url=os.getenv('REDIS_URL', 'redis://localhost'))

if __name__ == '__main__':
  logging.info('Started')
  my_ip = get_my_ip()
  # enable CORS
  CORS(app, resources={r'/*': {'origins': '*'}})
  logging.info("Connect to http://{}:5000/".format(my_ip))
  app.run(host="0.0.0.0", port=5000, debug=True)
