import json
from conductores import Conductor


def cargar_registro_oficial(archivo_registro_oficial):
    '''
    Carga el registro oficial de conductores en Chile. No deben hacer nada
    con este método.
    '''
    registro_oficial = dict()
    with open(archivo_registro_oficial, 'r') as file:
        registros = json.load(file)
        for nombre_conductor, patente in registros.items():
            registro_oficial[nombre_conductor] = patente
    return registro_oficial

def cargar_conductores(archivo_conductores):
    '''
    Carga a los conductores del path en el atributo self.conductores. No
    deben hacer nada con este método.
    '''
    conductores = list()
    with open(archivo_conductores, 'r', encoding="latin-1") as file:
        for line in file:
            conductor = Conductor(*line.strip().split(","))
            conductores.append(conductor)
    return conductores


def cargar_datos(archivo_registro_oficial, archivo_conductores):
    '''
    Pobla el sistema utilizando las funciones dadas.
    Recuerden manejar el caso de que se levante algún error.
    '''
    registro_oficial = None
    conductores = None

    return registro_oficial, conductores
