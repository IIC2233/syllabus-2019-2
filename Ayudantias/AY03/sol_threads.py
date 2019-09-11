import threading as thr
import time
import random


class Jorry(thr.Thread):
    def __init__(self, x, y):
        # Siempre debos inicializar el super cuando heredamos
        super().__init__()
        self.x = x
        self.y = y

    def mover(self):
        mov = int(input("Ingresa la cantidad de casillas: "))
        self.x += mov
        self.y += mov
        print(f'Jorry se movió a {self.x}, {self.y}\n')

    def run(self):
        for i in range(3):
            self.mover()
            time.sleep(1)


class MrMeeseeks(thr.Thread):
    def __init__(self, numero, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.numero = numero

    def mover(self):
        mov = random.randint(1, 2)
        self.x += mov
        self.y += mov
        print(f'El Mr Meeseeks{self.numero} se movió a {self.x}, {self.y}\n')

    def run(self):
        for i in range(3):
            self.mover()
            time.sleep(1)


if __name__ == "__main__":
    meeseeks1 = MrMeeseeks("1", 0, 0)
    meeseeks2 = MrMeeseeks("2", 0, 0)
    jorry = Jorry(0, 0)

    meeseeks1.start()
    meeseeks2.start()
    jorry.start()
