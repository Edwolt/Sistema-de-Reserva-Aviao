import threading


class Poltrona:
    def __init__(self): # inicializa a poltrona como livre
        self.client = None
        self.semaphore = threading.Semaphore()

    def reserva(self, client) -> bool:
        self.semaphore.acquire()
        if self.client is None: # se a poltrona estiver livre, atualiza o cliente na poltrona e retorna true para a reserva
            self.client = client

            self.semaphore.release()
            return True
        else: # se a poltrona estiver ocupada retorna false para a reserva
            self.semaphore.release()
            return False


class Aviao:
    def __init__(self, n=60): # inicializa as 60 poltronas do aviao
        self.poltronas = [Poltrona() for _ in range(n)]

    def livres(self) -> list[bool]: # retorna lista com as poltronas livres do aviao
        res = []
        for p in self.poltronas: # checa cada poltrona e coloca nas lista as que estao lires
            p.semaphore.acquire()
            res.append(p.client is None)
            p.semaphore.release()

        return res
    
    def reserva(self, poltronas_desejadas, identificador):
        retorno = [] # Lista com True para sucesso e False para fracasso.

        for indice in poltronas_desejadas: # checa cada poltrona desejada
            poltrona = self.poltronas[indice]
            poltrona.semaphore.acquire()
            if poltrona.client is None: # se a poltrona estiver livre, atualiza o cliente na poltrona e retorna true para a reserva
                poltrona.client = identificador
                poltrona.semaphore.release()
                retorno.append(True)
            else: # se a poltrona estiver ocupada retorna false para a reserva
                poltrona.semaphore.release()
                retorno.append(False)
    
        return retorno

    def cancela_reserva(self, poltronas_nao_desejadas, identificador):
        retorno = [] # Lista com True para sucesso e False para fracasso

        for indice in poltronas_nao_desejadas: # checa cada poltrona nao desejada
            poltrona = self.poltronas[indice]
            poltrona.semaphore.acquire()
            if poltrona.client == identificador: # se a poltrona estiver ocupada pelo cliente, atualiza a poltrona para livre retorna true para o cancelamento
                poltrona.client = None
                poltrona.semaphore.release()
                retorno.append(True)
            else: # se a poltrona estiver livre ou ocupada por outro cliente retorna false para o cancelamento
                poltrona.semaphore.release()
                retorno.append(False)

        return retorno
