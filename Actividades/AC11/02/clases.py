from random import randint
from time import sleep
from threading import Lock, Thread, Event
from math import log2

class Critico(Event, Thread):
    def __init__(self):
        Thread.__init__(self, daemon=True)
        Event.__init__(self)
        self.start()

    def run(self):
        while True:
            sleep(randint(10, 100) / 10)
            self.set()


class Entrenador:

    critico = Critico()

    def __init__(self, nombre):
        self.nombre = nombre
        self.hp_programon_original = randint(100, 200)
        self.hp_programon = self.hp_programon_original
        self.ataque_programon = randint(90, 120)
        self.defensa_programon = randint(80, 100)

    def atacar(self, enemigo):
        # [Completar/Modificar] para poder dar ataques críticos

        # recuerda usar la clase instanciada "critico"
        
        dano = round(20 * self.ataque_programon / enemigo.defensa_programon)
        enemigo.hp_programon -= dano
        print(f'{self} ataca {dano} a {enemigo}')

    def sanar(self):
        self.hp_programon = self.hp_programon_original

    def __repr__(self):
        return f'({self.nombre} HP:{self.hp_programon})'

class Batalla(Thread):

    id_actual = 1
    # Puedes agregar atributos de clase

    def __init__(self):
        super().__init__()
        # print('¡Batalla creada!')
        self.id = Batalla.id_actual
        Batalla.id_actual += 1
        self.oponente_1 = None
        self.oponente_2 = None
        self.ganador = None
        # Puedes agregar atributos de instancia

    def run(self):
        # Completar/Moficiar

        # Si tiene batallas pendientes, debe esperar a que terminen.
        print(f'{self} esperando batallas...')

        print(f'{self} lista para comenzar.')
        self.realizar_batalla()
    
    def realizar_batalla(self):
        # Puedes agregar líneas si lo encuentras necesario.
        # Intentar mantener el flujo de las batallas intacto.
        print(f'----------¡Comienza batalla {self.id}! A {int(log2(self.id))} de final----------')
        print(f'{self.oponente_1} versus {self.oponente_2}')
        while self.oponente_1.hp_programon > 0 and self.oponente_2.hp_programon > 0:
            #
            # Completar una ronda
            #
            sleep(1)
        if self.oponente_1.hp_programon <= 0:
            self.ganador = self.oponente_2
        else:
            self.ganador = self.oponente_1
        self.ganador.sanar()
        print(f'----------¡Gana {self.ganador}!----------')
        

    def __repr__(self):
        return f'Batalla {self.id}'