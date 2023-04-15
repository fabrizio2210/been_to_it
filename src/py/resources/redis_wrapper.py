import os
import werkzeug
import logging
import json
from flask_restful import Resource, reqparse
from cache.redis_wrapper import RedisWrapper, slowdown


class Cache(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('values',
                      type=str,
                      required=False,
                      help="Value to put in memory."
                      )
  parser.add_argument('Authorization',
                      type=str,
                      required=True,
                      location='headers',
                      help="User identifier."
                      )

  def post(self):
    data = Cache.parser.parse_args()
    if data['Authorization'] == os.getenv('CACHE_TOKEN'):
      values = json.loads(data['values'])
      pipe = RedisWrapper.client.pipeline()
      r_index = 1
      for row in values:
        for col in range(15):
          if col < len(row):
            RedisWrapper.commandToWriteCache(cell=(chr(ord('A')+col), r_index),
                                             pipe=pipe,
                                             value=row[col])
          else:
            RedisWrapper.commandToWriteCache(cell=(chr(ord('A')+col), r_index), 
                                             pipe=pipe,
                                             value=None)
        r_index += 1
      pipe.execute()
      slowdown()

      return {'cache': RedisWrapper.readCacheToWrite()}, 200
    else:
      logging.debug("Authorization:%s", data['Authorization'])
      logging.debug("CACHE_TOKEN:%s",  os.getenv('CACHE_TOKEN'))
      return {'message': 'forbidden'}, 401


