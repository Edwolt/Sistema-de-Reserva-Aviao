import socket
import PySimpleGUI as sg


class Janela:
    def __init__(self, name):
        self.layout = [
            [sg.Text("Assentos")],
            [sg.Text("O") for i in range(30)],
            [sg.Input()],
        ]
        self.window = sg.Window(f"Cliente {name}", self.layout)

    def read(self):
        return self.window.read()


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    janela = Janela(host)

    while True:
        event, values = janela.read()
        if event == sg.WIN_CLOSED or values == "Exit":
            client_socket.send("2".encode())
            break

        client_socket.send("0".encode())
        data = client_socket.recv(1024).decode
        print(data)

    # while message.lower().strip() != "bye":
    #     client_socket.send(message.encode())  # send message
    #     data = client_socket.recv(1024).decode()  # receive response

    #     print("Received from server: " + data)  # show in terminal

    #     message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == "__main__":
    client_program()
