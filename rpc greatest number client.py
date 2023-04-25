import xmlrpc.client

# Create an XML-RPC server proxy
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

# Define the three numbers
num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))
num3 = int(input("enter 3rd number: "))

# Call the remote function to find the greatest number
result = proxy.find_greatest(num1, num2, num3)

# Print the result
print(f"The greatest number is: {result}")