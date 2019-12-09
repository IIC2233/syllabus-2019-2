import json


class Programon:
    def __init__(self, nombre, movimientos, movs_huevo, grupos_huevo):
        self.nombre = nombre
        self.movimientos = movimientos
        self.movs_huevo = movs_huevo
        self.grupos_huevo = grupos_huevo
    
    def __hash__(self):
        return hash(self.nombre)
    
    def __str__(self):
        return (f'Mon(nombre="{self.nombre}"", movs={self.movimientos},'
                f'movs_huevo={self.movs_huevo}, grupos_huevo={self.grupos_huevo})')
    
    def __repr__(self):
        return f'Mon(nombre="{self.nombre}", ... )'


class GrupoHuevo:

    def __init__(self, nombre, programones):
        self.nombre = nombre
        self.programones = programones
    
    def __hash__(self):
        return hash(self.nombre)

    def __str__(self):
        return f'GrupoHuevo(nombre="{self.nombre}", mons={self.programones}'

    def __repr__(self):
        return f'GrupoHuevo(nombre="{self.nombre}", ... )'


def cargar_grafo(ruta):
    '''
        programones: un diccionario.
            key: nombre del PROGRáMON (string)
            value: instancia de Programon
        
        grupos_huevo: un diccionario.
            key: nombre del GRUPO HUEVO (string)
            value: instancia de GrupoHuevo
    '''
    
    with open(ruta, 'r', encoding='utf-8') as archivo:
        mons_cargados = json.load(archivo)
    
    programones = {}
    grupos_huevo = {}
    
    # Completar
    
    return programones, grupos_huevo


def comprobar_cadena(grafo, cadena, movimiento):
    cadena = [grafo[nombre] for nombre in cadena]
    if movimiento not in cadena[-1].movimientos:
        print(f'{cadena[-1]} no aprende movimiento naturalmente')
        return False
    actual = cadena.pop()
    while len(cadena) > 0:
        siguiente = cadena.pop()
        if movimiento not in siguiente.movs_huevo:
            print(f'{siguiente} no aprende movimiento por huevo')
            return False
        if len(set(siguiente.grupos_huevo) & set(actual.grupos_huevo)) == 0:
            print(f'{actual} y {siguiente} no tienen grupo huevo en común')
            return False
        actual = siguiente
    return True


def movimiento_posible(grafo, programon, movimiento):
    ## Completar
    pass



if __name__ == '__main__':
    grafo, grupos_huevo = cargar_grafo('programon.json')

    print(comprobar_cadena(grafo, ['SKITTY', 'SPINDA', 'GOTHITA'], 'FAKETEARS'))
    
    print(movimiento_posible(grafo, 'SKITTY', 'FAKETEARS'))
