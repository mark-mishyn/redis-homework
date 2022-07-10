import math
from random import random

def get_from_db(ttl: int) -> bool:
     """
     If ttl is close to expire than probabylity to get from cache is decreased.
     Examples: 
     1) if ttl is 90 seconds -- low DB query chanse
     2) if ttl is 5 seconds -- 50/50 DB query chanse
     3) if ttl is 0.5 seconds -- high DB query chanse
     """
     if ttl >= 100:
         return False
     if ttl < 0.1:
          return True
     prob = math.log(ttl / 100) * -15
     return (random() * 100) < prob

def get_from_cache(key: str):
     ttl = r.ttl(key)
     if not get_from_cache(ttl):
          return r.get(key)

