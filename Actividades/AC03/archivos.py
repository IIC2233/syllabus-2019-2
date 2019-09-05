from yoNube import descargar
from decodificador import decodificar

from collections import namedtuple
import os


# ------ ESTRUCTURAS ------

Cancion = namedtuple("Cancion", ["id", "nombre", "id_artista", "duracion"])
Artista = namedtuple("Artista", ["id", "nombre", "genero", "ano_formacion"])
Usuario = namedtuple("Usuario", ["nombre", "username", "fecha_ingreso"])
Rating = namedtuple("Rating", ["username", "id_cancion", "rating"])

# ----- DECORADOR -------


def desencriptar(funcion_decodificadora, tipo_archivo):
    """
    Decorador que permite desencriptar las bases de datos.

    La desencriptación requiere de una función decodificadora.
    """
    # Este es el código base del decorador y es completamente editable
    def decorador(funcion_a_decorar):
        def wrapper(*args, **kwargs):
            return funcion_a_decorar(*args, **kwargs)
        return wrapper
    return decorador


# ------------------------------------------------------------

# --------- NO MODIFICAR LAS FUNCIONES, SOLO DECORAR ---------

# ------------------------------------------------------------


@desencriptar(decodificar, "canciones")
def leer_canciones(path):
    """
    Esta función recibe una ruta (path) y retorna un generador con los datos.

    Nota que es cada línea se divide por las comas, por lo tanto entrega
    5 elementos.

    Decorar para:
    =============
    - Desencriptar los datos.
    - Entregar las instancias correspondientes.
    """
    with open(path, 'r', encoding = 'utf-8') as archivo:
        for linea in archivo:
            yield linea.strip().split(',')


@desencriptar(decodificar, "artistas")
def leer_artistas(path):
    """
    Esta función recibe una ruta (path) y retorna un generador con los datos.

    Nota que es cada línea se divide por las comas, por lo tanto entrega
    4 elementos.

    Decorar para:
    =============
    - Desencriptar los datos.
    - Entregar las instancias correspondientes.
    """
    with open(path, 'r', encoding = 'utf-8') as archivo:
        for linea in archivo:
            yield linea.strip().split(',')


@desencriptar(decodificar, "usuarios")
def leer_usuarios(path):
    """
    Esta función recibe una ruta (path) y retorna un generador con los datos.

    Nota que es cada línea se divide por las comas, por lo tanto entrega
    3 elementos.

    Decorar para:
    =============
    - Desencriptar los datos.
    - Entregar las instancias correspondientes.
    """
    with open(path, 'r', encoding = 'utf-8') as archivo:
        for linea in archivo:
            yield linea.strip().split(',')


@desencriptar(decodificar, "ratings")
def leer_ratings(path):
    """
    Esta función recibe una ruta (path) y retorna un generador con los datos.

    Nota que es cada línea se divide por las comas, por lo tanto entrega
    3 elementos.

    Decorar para:
    =============
    - Desencriptar los datos.
    - Entregar las instancias correspondientes.
    """
    with open(path, 'r', encoding = 'utf-8') as archivo:
        for linea in archivo:
            yield linea.strip().split(',')


if __name__ == "__main__":
    ruta_canciones = os.path.join("data_base", "canciones.csv")
    canciones = leer_canciones(ruta_canciones)
    ruta_artistas = os.path.join("data_base", "artistas.csv")
    artistas = leer_artistas(ruta_artistas)
    ruta_usuarios = os.path.join("data_base", "usuarios.csv")
    usuarios = leer_usuarios(ruta_usuarios)
    ruta_ratings = os.path.join("data_base", "ratings.csv")
    ratings = leer_ratings(ruta_ratings)

    generadores = [canciones, artistas, usuarios, ratings]

    for gen in generadores:
        print(f"\nProbando generador : ")
        print(next(gen))
        print(next(gen))
        print(next(gen))
        print(next(gen))
