import socket

def socket_server(file_name, host='0.0.0.0', port=12345):
    # create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to a specific address and port
    server_address = (host, port)
    print('starting up on {} port {}'.format(*server_address))
    server_socket.bind(server_address)

    # listen for incoming connections
    server_socket.listen(1)
    print('waiting for a connection')

    # wait for a client to connectp
    connection, client_address = server_socket.accept()
    print('connection from', client_address)

    file = open(file_name, 'rb')
    file_data = file.read(1024)
    connection.send(file_data)

def send_video(file_name, host='0.0.0.0', port=12345):
    # create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to a specific address and port
    server_address = (host, port)
    print('starting up on {} port {}'.format(*server_address))
    server_socket.bind(server_address)

    # listen for incoming connections
    server_socket.listen(1)
    print('waiting for a connection')

    # wait for a client to connect
    connection, client_address = server_socket.accept()
    print('connection from', client_address)

    with open(file_name, 'rb') as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            connection.sendall(chunk)

def receive_video(file_name, host='0.0.0.0', port=12345):
    # create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to a specific address and port
    server_address = (host, port)
    print('starting up on {} port {}'.format(*server_address))
    server_socket.bind(server_address)

    # listen for incoming connections
    server_socket.listen(1)
    print('waiting for a connection')

    # wait for a client to connect
    connection, client_address = server_socket.accept()
    print('connection from', client_address)

    with open(file_name, 'wb') as f:
        while True:
            chunk = connection.recv(1024)
            if not chunk:
                break
            f.write(chunk)

    print("received successfully")

    connection.close()
    server_socket.close()

if __name__ == '__main__':
    #send_video('video/test_video.mov')
    receive_video('video/receive.mov')
