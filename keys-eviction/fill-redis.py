import redis

r = redis.Redis(host='localhost', port=6379, db=0)
for i in range(10):
	print(i)
	r.set(f'some-very-long-key-goes-here-{i}', f'{1000 * "some-long-value-goes-here"}-{i}')
