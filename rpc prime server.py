import xmlrpc.server

# function to check if a number is prime or not
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# create an RPC server
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))

# register the is_prime function with the server
server.register_function(is_prime, "is_prime")

# start the server
server.serve_forever()