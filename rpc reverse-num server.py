import xmlrpc.server

def rev(num):
    rev_num = 0
    while num!=0:
        digit = num%10
        rev_num = rev_num *10 + digit
        num //= 10
    return rev_num

# Create an XML-RPC server and register the function
server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000))
server.register_function(rev, 'rev')

# Start the server
print('Server listening on port 8000...')
server.serve_forever()