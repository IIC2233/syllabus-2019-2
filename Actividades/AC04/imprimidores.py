from threading import Thread, Lock
from utils import reloj
import random


class Imprimidor(Thread):

    def __init__(self, nombre, berlin, bolsa_dinero):
        super().__init__()
        pass

    def run(self):
        '''
        Funcionalidad de iMPRIMIDOR que imprime dinero cada 5 minutos, cada
        iteracion chequea si se cumple que hay problema con el dinero (20%)
        '''
        pass

    def imprimir_dinero(self, dinero):
        '''
        Llamar a este método para imprimir dinero.
        ***Acá debes procurarte de evitar errores de concurrencia***
        :param dinero:
        :return:
        '''
        pass

    def problema_papel(self):
        '''
        Probabilidad de problema con el papel de 20%
        '''
        pass
