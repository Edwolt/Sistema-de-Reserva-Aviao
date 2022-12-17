import socket
import PySimpleGUI as sg


def create_janela(name):
    layout = [
        [sg.Text("Assentos")],
        [sg.Text(".", key=f"-ITEM{i}-") for i in range(30)],
        [sg.Input()],
    ]
    return sg.Window(f"Cliente {name}", layout, finalize=True)


def update_assentos(janela, data):
    for i, val in enumerate(data):
        print(i, val)
        janela[f"-ITEM{i}-"].update(val)


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
        if event == sg.WIN_CLOSED or values == "Exit":
            client_socket.send("2".encode())
            break

        client_socket.send("0".encode())
        data = client_socket.recv(1024).decode()
        print("Atualiza")
        update_assentos(janela, data)

    janela.close()
    client_socket.close()  # close the connection


if __name__ == "__main__":
    client_program()
