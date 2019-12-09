import json
from textwrap import indent


class NodoProgramon:

    def __init__(self, numero, nombre):
        self.numero = numero
        self.nombre = nombre
        self.hije_izquierdo = None
        self.hije_derecho = None

    def tiene_hije_izquierdo(self):
        return True if self.hije_izquierdo else False

    def tiene_hije_derecho(self):
        return True if self.hije_derecho else False

    def __repr__(self):
        texto = f'{self.numero}. {self.nombre} \n'
        repr_hijos = []
        izq = 'Izq: '
        izq += repr(self.hije_izquierdo) if self.tiene_hije_izquierdo() else '-'
        der = 'Der: '
        der += repr(self.hije_derecho) if self.tiene_hije_derecho() else '-'
        repr_hijos.append(izq)
        repr_hijos.append(der)
        texto_hijos = [indent(texto_hijo, '   ') for texto_hijo in repr_hijos]
        return texto + '\n'.join(texto_hijos)


class ProgramonTree:

    '''Estructura que almacena NodoProgramones.'''

    def __init__(self):
        self.raiz = None

    def cargar_nodos(self, ruta):
        with open(ruta) as archivo:
            datos = json.load(archivo)
        for programon in datos:
            nodo_programon = NodoProgramon(**programon)
            self.insertar_programon(nodo_programon)
            # Cada vez que agrega un nodo se imprime para ver como está.
            print(self) 
            print()

    def insertar_programon(self, programon):
        if self.raiz == None:
            self.raiz = programon
        else:
            # Completar
            pass

    def numero_programon(self, nombre):
        por_visitar = []
        por_visitar.append(self.raiz)

        # Completar

        return numero
    
    def ruta_programon(self, nombre):
        numero = self.numero_programon(nombre)
        nodo_actual = self.raiz
        ruta = [nodo_actual.numero]
        nodo_encontrado = False
        while not nodo_encontrado:
            pass
            # Completar
        return ruta

    def __repr__(self):
        return repr(self.raiz)


if __name__ == '__main__':
    programontree = ProgramonTree()
    programontree.cargar_nodos('programones.json')
    print(programontree)

    print(programontree.numero_programon('Pidgeot'))
    print(programontree.ruta_programon('Pidgeot'))

    print(programontree.numero_programon('Bulbasaur'))
    print(programontree.ruta_programon('Bulbasaur'))

    print(programontree.numero_programon('Ekanz'))
    print(programontree.ruta_programon('Ekanz'))