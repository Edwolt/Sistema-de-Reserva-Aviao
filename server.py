import socket
import threading


def server_thread(conn, address, name):
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        print("from connected user: " + str(data))
        data = input(" -> ")
        conn.send(data.encode())  # send data to the client
    conn.close()  # close the connection


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    try:
        # configure how many client the server can listen simultaneously
        server_socket.listen(10)
        id = 1
        while True:
            conn, address = server_socket.accept()  # accept new connection
            print("Connection from: " + str(address))
            new_thread = threading.Thread(
                target=server_thread, args=(conn, address, f"Client {id}")
            )
            new_thread.start()
            id += 1
    except KeyboardInterrupt:
        pass

    print("exited server...")
    server_socket.shutdown(socket.SHUT_RDWR)


if __name__ == "__main__":
    server_program()
