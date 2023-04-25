import xmlrpc.client

# create an RPC proxy to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

# call the is_prime function on the server
n = int(input("enter number: "))
result = proxy.is_prime(n)

# print the result
print(result)