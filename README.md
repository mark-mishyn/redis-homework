# redis-homework

### Keys Eviction
Here we are using simplest Redis setup. File redis.conf sets max memory to 1mb.  
There is a python script with fucntions to test 6 keys evistion policies:
1. allkeys-random
2. allkeys-lru
3. allkeys-lfu
4. volatile-lru
5. volatile-lfu
6. volatile-ttl

### Probabalistic Cache Getter
There is a python script with function that allows to get value from cache or return None if key is *pseudo* expired. The smalled ttl leads to bigger chance to re-set value to cache.


### Redis Cluster
Simple Docker-compose with Redis master, slave and sentinel nodes