import socket
import threading
import PySimpleGUI as sg

colunas = 'ABCDEF'
numero_assentos = 60
delay_update = 1.0

def id_para_poltrona(id): # retorna linha e coluna da poltrona
    return str(id//6) + colunas[id%6]

def create_janela(name): # cria uma janela
    layout = [[sg.Text("Assentos")]] + [[sg.Button(colunas[i%6], key = ("assento", i), button_color = ('white','green')) for i in range(j,j+3)] + [sg.Text("{:0>2d}".format(1 + (j//6)))] + [sg.Button(colunas[i%6], key = ("assento", i), button_color = ('white','green')) for i in range(j+3,j+6)] for j in range(0,numero_assentos,6)]
    return sg.Window(f"Cliente {name}", layout, finalize=True)

def thread_update(client_socket, janela): # atualiza a thread a cada segundo
    janela.write_event_value("update", "timer")
    t = threading.Timer(delay_update, thread_update, args=(client_socket,janela))
    t.daemon = True
    t.start()

def update_assentos(janela, data): # atualiza as cores da poltronas
    for i, val in enumerate(data):
        if janela[("assento",i)].ButtonColor != ('white','blue'):
            janela[("assento",i)].update(button_color= ('white','green') if val == 'L' else ('white','red'))

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5100  # socket server port number
    
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    janela = create_janela(host)
    data = client_socket.recv(1024).decode()
    update_assentos(janela, data)

    # comeca a atualizar a thread a cada segundo
    t = threading.Timer(delay_update, thread_update, args=(client_socket,janela))
    t.daemon = True
    t.start()

    while True:
        event, values = janela.read()

        # caso a janela seja fechada
        if event == sg.WIN_CLOSED or values == "Exit":
            client_socket.send("Q".encode())
            break

        if event[0] == "assento":
            # Assento Vazio
            if janela[event].ButtonColor == ('white','green'):
                client_socket.send("1{}".format(event[1]).encode())
                data = client_socket.recv(1024).decode()
                if data[0] == '1':
                    janela[event].update(button_color = ('white','blue'))

            # Assento Ocupado por outro Cliente
            elif janela[event].ButtonColor == ('white','red'):
                pass
            
            # Assento Ocupado pelo próprio Cliente
            else:    
                client_socket.send("2{}".format(event[1]).encode())
                data = client_socket.recv(1024).decode()
                janela[event].update(button_color = ('white','green'))

        client_socket.send("0".encode())
        data = client_socket.recv(1024).decode()
        update_assentos(janela, data)

    janela.close()
    client_socket.close()  # close the connection


if __name__ == "__main__":
    client_program()
