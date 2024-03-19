from pyignite import Client

client = Client()
client.connect('127.0.0.1', 10800)

#Create cache
my_cache = client.create_cache('my cache')

#Put value in cache
my_cache.put(1, 'Hello World')

#Get value from cache
result = my_cache.get(1)
print(result)