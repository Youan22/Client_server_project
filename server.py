import socket
import requests
import json
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

def get_weather():
    api_key = "04520f875170246d4b14dc5109111cdb"
    city = 'London'  # You can change the city here
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = json.loads(response.text)
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    temperature = round(temperature - 273.15, 2)  # Convert temperature from Kelvin to Celsius
    return f'{weather}, Temperature: {temperature}°C'

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 5000)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print('Server listening on {}:{}'.format(*server_address))

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print('Accepted connection from {}:{}'.format(*client_address))

        # Receive data from the client
        data = client_socket.recv(1024).decode()
        print('Received message: {}'.format(data))

        # Process the data and generate the response
        if data == 'time':
            response = get_current_time()
        elif data == 'date':
            response = get_current_date()
        elif data == 'weather':
            response = get_weather()
        else:
            response = 'Unknown request'

        # Send the response back to the client
        client_socket.send(response.encode())
        print('Sent response: {}'.format(response))

        # Close the client connection
        client_socket.close()

if __name__ == '__main__':
    main()
