import csv
from conductores import Conductor
from excepcion_patente import ErrorPatente
import os

class DCConductor:

    def __init__(self, registro_oficial, conductores):
        '''
        El constructor crea las estructuras necesarias para almacenar los datos
         proporcionados, recibe la información necesaria para el funcionamiento de la clase.
        '''
        self.registro_oficial = registro_oficial
        self.conductores = conductores
        self.seleccionados = list()


    def chequear_rut(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su rut no siga
        el formato correcto
        '''
        pass


    def chequear_nombre(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su nombre no
        exista en el registro oficial.
        '''
        pass


    def chequear_celular(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su celular
        no siga el formato correcto
        '''
        pass


    def chequear_patente(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su patente no
        coincida con la información del registro oficial.
        '''
        pass
