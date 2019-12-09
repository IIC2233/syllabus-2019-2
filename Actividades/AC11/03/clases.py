from bugterpie import Bugterpie
import json


indices_generaciones = {
    1: (1, 151),
    2: (152, 251),
    3: (252, 386),
    4: (387, 493),
    5: (494, 649)
}


class Programon:
    def __init__(self, id, nombre, tipo, generacion):
        self.id = int(id)
        self.nombre = nombre
        self.tipo = tipo
        self.generacion = int(generacion)

    def __repr__(self):
        return f'PROGRáMON N°{self.id:0>3}: {self.nombre}'


class Pydgey:
    def __init__(self, path_data):
        self.data = None
        self.cargar_data(path_data)

    def cargar_data(self, path_data):
        with open(path_data, 'r', encoding='utf-8') as file:
            self.data = json.load(file, object_hook=lambda x: Programon(**x))

    @staticmethod
    def aire_afilatipo(programon):
        '''
        Acá debes completar el método aire_afilatipo
        '''
        pass

    @staticmethod
    def pico_taladraid(programon):
        '''
        Acá debes completar el método pico_taladraid
        '''
        pass

    @staticmethod
    def remolinombre(programon):
        '''
        Acá debes completar el método remolinombre
        '''
        pass

    def encontrar_errores(self):
        for programon in self.data:
            print(f'>> Se procesa {programon}')
            try:
                self.aire_afilatipo(programon)

            except TypeError as err:
                '''
                Acá debes manejar la excepción del aire_afilatipo
                '''
                print(err)

            try:
                self.pico_taladraid(programon)

            except IndexError as err:
                '''
                Acá debes manejar la excepción del pico_taladraid
                '''
                print(err)

            try:
                self.remolinombre(programon)

            except Bugterpie as err:
                '''
                Acá debes manejar la excepción del remolinombre
                '''
                print(err)
