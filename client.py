import socket
import PySimpleGUI as sg


def create_janela(name):
    layout = [
        [sg.Text("Assentos")],
        [sg.Button(".", key=("assento", i)) for i in range(30)],
    ]
    return sg.Window(f"Cliente {name}", layout, finalize=True)


def update_assentos(janela, data):
    for i, val in enumerate(data):
        janela[("assento", i)].update(val)


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    janela = create_janela(host)
    data = client_socket.recv(1024).decode()
    update_assentos(janela, data)

    while True:
        event, values = janela.read()

        client_socket.send("0".encode())
        data = client_socket.recv(1024).decode()
        update_assentos(janela, data)

        if event == sg.WIN_CLOSED or values == "Exit":
            client_socket.send("Q".encode())
            break

        if event[0] == "assento":
            client_socket.send("1{}".format(event[1]).encode())
            data = client_socket.recv(1024).decode()

        client_socket.send("0".encode())
        data = client_socket.recv(1024).decode()
        update_assentos(janela, data)

    janela.close()
    client_socket.close()  # close the connection


if __name__ == "__main__":
    client_program()
