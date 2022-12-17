import threading


class Poltrona:
    def __init__(self):
        self.client = None
        self.semaphore = threading.Semaphore()

    def reserva(self, client) -> bool:
        self.semaphore.acquire()
        if self.client is None:
            self.client = client

            self.semaphore.release()
            return True
        else:
            self.semaphore.release()
            return False


class Onibus:
    def __init__(self, n=30):
        self.poltronas = [Poltrona() for _ in range(n)]

    def ocupado(self) -> list[bool]:
        res = []
        for p in self.poltronas:
            p.semaphore.acquire()
            res.append(p.client is not None)
            p.semaphore.release()

        return res
