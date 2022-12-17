import threading

class Poltrona:
    def __init__(self):
        self.client = None
        self.semaphore = threading.Semaphore()

    def reserva(self, client) -> bool:
        with self.semaphore:
            # acquire semaphore
            if self.client == None:
                self.client = client
                return True

        return False
        # close semaphore

# TODO Talvez dê só para criar a lista sem ter a classe Onibus
class Onibus:
    def __init__(self, n=30):
        self.poltronas = [Poltrona for _ in range(n)]
