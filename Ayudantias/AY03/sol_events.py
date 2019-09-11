import threading as thr
import time
import random


class Jorry(thr.Thread):
    def __init__(self, x, y, move_event):
        super().__init__()
        self.x = x
        self.y = y
        self.move_event = move_event  # Definimos el evento

    def mover(self):
        mov = int(input("Ingresa la cantidad de casillas: "))
        self.move_event.set()  # Jorry se movió y se activa el evento
        self.x += mov
        self.y += mov
        print(f'Jorry se movió a {self.x}, {self.y}\n')

    def run(self):
        for i in range(1):
            self.mover()
            time.sleep(1)


class MrMeeseeks(thr.Thread):
    def __init__(self, numero, x, y, start_event):
        super().__init__()
        self.x = x
        self.y = y
        self.numero = numero
        self.start_event = start_event  # Agragamos el evento

    def mover(self):
        mov = random.randint(1, 2)
        self.x += mov
        self.y += mov
        print(f'El Mr Meeseeks{self.numero} se movió a {self.x}, {self.y}\n')

    def run(self):
        self.start_event.wait()  # Esperamos a que ocurra el evento para partir
        for i in range(3):
            self.mover()
            time.sleep(1)


if __name__ == "__main__":
    jorry_se_mueve = thr.Event()

    meeseeks1 = MrMeeseeks(1, 0, 0, jorry_se_mueve)
    meeseeks2 = MrMeeseeks(2, 0, 0, jorry_se_mueve)
    jorry = Jorry(0, 0, jorry_se_mueve)

    jorry.start()
    meeseeks1.start()
    meeseeks2.start()
