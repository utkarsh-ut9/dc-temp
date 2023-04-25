# Initialize server list and request count
servers = ['server1', 'server2', 'server3', 'server4', 'server5']
request_count = [0, 0, 0, 0, 0]
# Define function to return server with least requests
def get_least_loaded_server():
    return servers[request_count.index(min(request_count))]
# Simulate requests to servers
for i in range(10):
    # Get least loaded server
    least_loaded_server = get_least_loaded_server()
    # Send request to least loaded server
    print(f'Sending request {i+1} to {least_loaded_server}')
    # Increment request count for least loaded server
    request_count[servers.index(least_loaded_server)] += 1