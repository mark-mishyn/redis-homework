FROM redis:6-alpine
  
RUN mkdir -p /redis
 
WORKDIR /redis
 
COPY sentinel.conf .
 
RUN chown redis:redis /redis/* 

EXPOSE 26379
 
ENTRYPOINT redis-server /redis/sentinel.conf --sentinel