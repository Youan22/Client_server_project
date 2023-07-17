import socket

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = ('localhost', 5000)
    client_socket.connect(server_address)
    print('Connected to {}:{}'.format(*server_address))

    # Send a request to the server
    request = input('Enter a request ("time", "date", or "weather"): ')
    client_socket.send(request.encode())

    # Receive and display the response
    response = client_socket.recv(1024).decode()
    print('Response: {}'.format(response))

    # Close the socket
    client_socket.close()

if __name__ == '__main__':
    main()
