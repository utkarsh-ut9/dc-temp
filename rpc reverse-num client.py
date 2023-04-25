import xmlrpc.client

# Create an XML-RPC server proxy
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

n = int(input())
result = proxy.rev(n)
print(f"The reversed number is: {result}")