from collections import namedtuple
from functools import reduce

caracteristicas = ['hp', 'ataque', 'defensa', 'velocidad', 'defensa_especial', 'ataque_especial']
Programon = namedtuple('PROGRáMON', ['id', 'nombre', 'tipo_1', 'tipo_2', *caracteristicas])

def obtener_lineas_archivo(ruta): 
    '''A partir de ruta de archivo TXT, retorna iterable con las líneas del archivo.'''
    # Implementado
    with open(ruta, 'rt', encoding='utf-8') as archivo:
        return archivo.readlines()

def obtener_programones(lineas): 
    '''A partir de líneas de texto, retorna un iterable con instancias de Programon.'''
    # Completar
    pass

def obtener_tipos(programones): 
    '''A partir de un iterable de programones, retorna un iterables de sus tipos sin 
    repeticiones.'''
    # Completar
    pass

def obtener_programones_de_tipo(programones, tipo):
    '''A partir de un iterable de programones y un tipo, retorna un iterable con aquellos 
    programones del tipo específicado.''' 
    # Completar
    pass

def obtener_cantidad_por_tipo(programones, tipos): 
    '''A partir de iterable de programones e iterable de tipos, retorna diccionario con llaves
    los tipos entregados y cuyos valores corresponden a la cantidad de programones de tal tipo.'''
    # Completar
    pass

def obtener_caracteristica_promedio(programones, caracteristica): 
    '''A partir de iterable de programones y el nombre de una característica de programon,
    entrega el valor promedio de tal caracteristica para los programones entregados.'''
    # Completar
    pass

def repr_lista(lista):
    '''A partir de una lista, genera su representación string para ser impreso.'''
    # Completar
    return ''



if __name__ == '__main__':

    lineas = obtener_lineas_archivo('programon.txt')
    
    # Probando obtener_programones
    programones = obtener_programones(lineas)
    print('Programones cargados:', len(programones))
    print('Algunos programones:')
    print(programones[0])
    print(programones[100])
    print(programones[648])
    print()

    # Probando obtener_tipos
    tipos = obtener_tipos(programones)
    print('Tipos encontrados:', len(tipos))
    print(tipos)
    print(repr_lista(tipos))
    print()

    # Probando obtener_programones_de_tipo
    hadas = obtener_programones_de_tipo(programones, 'Hada')
    print('Hadas encontradas:', len(hadas))
    print('Algunas hadas:')
    print(hadas[0])
    print(hadas[10])
    print(hadas[21])
    print()

    # Probando obtener_cantidad_por_tipo
    cantidad_por_tipo = obtener_cantidad_por_tipo(programones, tipos)
    print('Diccionario de cantidad por tipo:')
    print(cantidad_por_tipo)
    print(repr_lista(list(cantidad_por_tipo.items())))
    print()

    # Probando obtener_caracteristica_promedio
    promedios_hadas = [
        (caracteristica, obtener_caracteristica_promedio(hadas, caracteristica))
        for caracteristica in caracteristicas
    ]
    print('Caracteristicas promedio de hadas:')
    print(promedios_hadas)
    print(repr_lista(promedios_hadas))
    