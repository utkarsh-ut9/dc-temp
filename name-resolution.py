import socket

def get_ip_add(url):
    try:
        host_name = socket.gethostbyname(url)
        host_ip = socket.gethostbyname(url)
        print("Hostname: ", host_name)
        print("IP: ", host_ip)
    except:
        print("Unable to get hostname and IP")

if __name__ == '__main__':
    url = input("Enter URL: ")
    get_ip_add(url)
