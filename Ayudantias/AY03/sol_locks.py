import threading as thr
import time
import random


class Jorry(thr.Thread):
    def __init__(self):
        super().__init__()
        self.hp = random.randint(50, 100)  # Seteamos la vida de Jorry

    def run(self):
        while self.hp > 0:
            print(f'Estúpidos meeseeks eso duele! Mi vida está en {self.hp}')
            time.sleep(1 / 2)
        print('RIP Jorry 2019')


class MrMeeseeks(thr.Thread):
    lock_jorry = thr.Lock()  # Creamos el lock como variable de clase

    def __init__(self, numero, jorry):
        super().__init__()
        self.daemon = True  # No pueden golpear a un Jorry muerto
        self.numero = numero
        self.jorry = jorry

    def atacar(self):
        ataque = random.randint(1, 3)
        self.jorry.hp -= ataque
        print(
            f'El Mr Meeseeks{self.numero} atacó a Jorry con un daño de {ataque}\n')

    def run(self):
        while True:
            with self.lock_jorry:  # Fijo el lock mientras mi thread Meeseek realiza el ataque
                self.atacar()
            time.sleep(1 / 2)


if __name__ == "__main__":
    jorry = Jorry()
    meeseeks1 = MrMeeseeks(1, jorry)
    meeseeks2 = MrMeeseeks(2, jorry)
    meeseeks3 = MrMeeseeks(3, jorry)
    meeseeks4 = MrMeeseeks(4, jorry)
    meeseeks5 = MrMeeseeks(5, jorry)

    jorry.start()
    meeseeks1.start()
    meeseeks2.start()
    meeseeks3.start()
    meeseeks4.start()
    meeseeks5.start()
