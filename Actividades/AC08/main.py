from cargar import cargar_archivos
from os import path


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id = id_usuario
        self.nombre = nombre
        self.seguidos = []
        # self.seguidores = [] # almacenar a los seguidores es opcional.


class Pintogram:
    def __init__(self):
        # Recuerda que debes almacenar todos los usuarios dentro de la red
        pass

    def nuevo_usuario(self, id_usuario, nombre):
        # Método que se encarga de agregar un usuario a la red
        pass

    def follow(self, id_seguidor, id_seguido):
        # Método que permite a un usuario seguir a otro
        pass

    def cargar_red(self, ruta_red):
        # Método que se encarga de generar la red social, cargando y
        # guardando cada uno de los usuarios. Quizás otras funciones de
        # Pintogram sean útiles.
        pass

    def unfollow(self, id_seguidor, id_seguido):
        # Método que pertmite a un usuario dejar de seguir a otro
        pass

    def mis_seguidos(self, id_usuario):
        # Método que retorna los seguidores de un usuario
        pass

    def distancia_social(self, id_usuario_1, id_usuario_2):
        # Método que retorna la "distancia social" de dos usuarios
        pass


if __name__ == "__main__":
    pintogram = Pintogram()
    pintogram.cargar_red(path.join("archivos", "simple.txt"))
    print(pintogram.mis_seguidos("1"))
    print(pintogram.mis_seguidos("3"))
    print(pintogram.distancia_social("3", "5"))

# Puedes agregar más consultas y utilizar los demás archivos para probar tu código
