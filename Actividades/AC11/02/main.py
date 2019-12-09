from random import shuffle
from clases import Entrenador, Batalla

def generar_entrenadores():
    nombres = [
        'itplanella', 'F-arellano', 'mariajesusbraun', 'fuentes145',
        'sebacarrasco', 'matiasmasjuan', 'Rafoxxa', 'JuaniAndres',
        'bahidalgo', 'mpbascunan', 'Baelfire18', 'JosefaPaz', 
        'sofiuni', 'fplois', 'cristozille', 'kisco99'
    ]
    shuffle(nombres)
    return [Entrenador(nombre) for nombre in nombres]

def generar_batallas(entrenadores):
    batallas = [Batalla() for _ in range(15)]
    for indice in range(0, 7):
        batalla = batallas[indice]
        sub_batalla_1 = batallas[2 * indice + 1]
        sub_batalla_2 = batallas[2 * indice + 2]
        batalla.oponente_1 = sub_batalla_1
        batalla.oponente_2 = sub_batalla_2
    for indice in range(7, 15):
        batalla = batallas[indice]
        batalla.oponente_1 = entrenadores.pop()
        batalla.oponente_2 = entrenadores.pop()
    return batallas

if __name__ == '__main__':
    entrenadores = generar_entrenadores()
    batallas = generar_batallas(entrenadores)
    for batalla in batallas:
        batalla.start()
    