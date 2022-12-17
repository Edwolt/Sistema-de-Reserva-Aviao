import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    try:
        # configure how many client the server can listen simultaneously
        server_socket.listen(2)
        conn, address = server_socket.accept()  # accept new connection
        conn2, address2 = server_socket.accept()
        print("Connection from: " + str(address))
        while True:

            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            data2 = conn2.recv(1024).decode()
            print("from connected user: " + str(data))
            print("from connected user 2: " + str(data2))
            data = input(' -> ')
            conn.send(data.encode())  # send data to the client
            conn2.send(data.encode())
        conn.close()  # close the connection
        conn2.close()
    except KeyboardInterrupt:
        pass

    server_socket.shutdown(socket.SHUT_RDWR)

if __name__ == '__main__':
    server_program()
