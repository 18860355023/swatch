import redis
import json
from settings import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD


redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=0, decode_responses=True)
login_redis = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=10, decode_responses=True)