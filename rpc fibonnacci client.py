import xmlrpc.client

# Create an XML-RPC server proxy
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

n = int(input("enter value of n: "))
result = proxy.fib(n)
print(f"The fibonnacci series upto n is: {result}")