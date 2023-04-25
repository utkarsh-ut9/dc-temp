import xmlrpc.server

# Define the function to find the greatest number
def find_greatest(num1, num2, num3):
    return max(num1, num2, num3)

# Create an XML-RPC server and register the function
server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000))
server.register_function(find_greatest, 'find_greatest')

# Start the server
print('Server listening on port 8000...')
server.serve_forever()