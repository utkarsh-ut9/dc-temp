import xmlrpc.client

# create an RPC proxy to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

# call the is_prime function on the server
result = proxy.is_prime(17)

# print the result
print(result)