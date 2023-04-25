import xmlrpc.server

def fib(n):
    num = n
    list = []
    n1, n2 = 0, 1
    list.append(n1)
    list.append(n2)
    print("Fibonacci Series:", n1, n2, end=" ")
    for i in range(2, num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        list.append(n3)
    return list

# Create an XML-RPC server and register the function
server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000))
server.register_function(fib, 'fib')

# Start the server
print('Server listening on port 8000...')
server.serve_forever()