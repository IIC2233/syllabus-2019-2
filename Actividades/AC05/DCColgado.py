from PyQt5.QtCore import QObject, pyqtSignal
from os.path import join
import random


with open("palabras.csv", "r", encoding="utf-8") as file:
    palabras = [line.strip() for line in file.readlines()]


def OBTENER_PALABRA():
    return random.choice(palabras)


'''
Clase Base para el juego.
Todos los elementos están para llegar y conectarlos.
Para entender el flujo del mismo existe el método juego_consola, que puede ser ejecutado
en este mismo script.

'''

class DCColgado(QObject):
    '''
    Señal a utilizar para el envio de
    la información necesaria para mostrar
    en tu Frontend
    '''
    respuesta_signal = pyqtSignal(dict)
    
    # ======== Para el bonus! =========
    end_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        
        # Diccionario con las imagenes listas para usar
        self.imagenes = {
            1: join("images", "1.png"),
            2: join("images", "2.png"),
            3: join("images", "3.png"),
            4: join("images", "4.png"),
            5: join("images", "5.png"),
            6: join("images", "6.png"),
            7: join("images", "7.png"),
            "win": join("images", "win.gif"),
            "lose": join("images", "lose.gif")
        }

        self.usadas = ""
        self.disponibles = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        self.palabra = ""
        self.palabra_actual = ""
        self.mensaje = ""
        self.intentos = 6
        self.ganador = False

        self.consola = False # NO MODIFICAR
    
    def check_info(self, data):
        """
        Funcion para manejar las solicitudes del Front-end.
        Pueden ser ingresar toda la palabra o solo una letra.
        La palabra es solo para el bonus.
        """
        if self.ganador or self.intentos == 0:
            # Siempre que aún no se haya ganado o perdido.
            self.actualizar_palabra()
        elif data["letra"] != "":
            self.check_letra(data["letra"])
        elif "palabra" in data and data["palabra"] != "":
            self.check_palabra(data["palabra"])
    
    def check_palabra(self, palabra):
        """
        Función para checkear si la palabra ingresada está correcta,
        si no, se pierde automáticamente.
        """
        if palabra.upper() == self.palabra:
            self.palabra_actual = " ".join(self.palabra)
            self.ganador = True
        else:
            self.intentos = 0

        # Se envía la actualización al Front-end
        self.actualizar_palabra()

    def check_letra(self, letra):
        """
        Función para checkear si la letra es correcta, es decir:
        - Si no se ha utilizado
        - Si la letra está en la palabra

        En caso de no cumplirse las condiciones, se descuenta un intento
        y se actualizan los atributos.
        """

        letra = letra.upper()

        if letra not in self.usadas:
            # Si la letra no se ha utilizado
            self.usadas += letra
            self.disponibles = self.disponibles.replace(letra, "   ")
            # Se marca como usada y se pasa a comporbar en la palabra

            if letra in self.palabra:
                self.mensaje = ""

            else:
                # Si no sirve, se marca el error.
                self.intentos -= 1
                self.mensaje = "La letra no está en la palabra"
        
        else:
            # Si ya se uso, se marca el error.
            self.mensaje = "La letra ya fue utilizada"
            self.intentos -= 1
        
        # Se envía al Front-end
        self.actualizar_palabra()
    
    def nueva_palabra(self):
        """
        Reinicia el juego con una nueva palabra al azar.
        """
        # Se genera una palabra random.
        # === Puedes agregar tu propia palabra para probar. ====
        palabra = OBTENER_PALABRA()

        # Se vuelve todo a los valores iniciales
        self.usadas = ""
        self.disponibles = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        self.palabra = palabra
        self.intentos = 6
        self.mensaje = ""
        self.ganador = False

        # Se envía al Front-end
        self.actualizar_palabra()

    def actualizar_palabra(self):
        '''
        Toma todos las letras usadas para actualizar la palabra y mostrar
        aquellas letras ya descubiertas.
        Posteriormente define el diccionario que enviará la información 
        necesaria al front-end.
        '''

        if self.ganador:
            self.mensaje = "Felicitaciones, has gandado!"
        elif self.intentos == 0:
            self.mensaje = "Que lastima, has perdido :("

            # ======== Para el bonus! =========
            self.end_signal.emit({"gif": self.imagenes["lose"]})

        data = {
            "msg": self.mensaje,
            "usadas": self.usadas,
            "disponibles": self.disponibles,
            "palabra": self.palabra_actual,
            "imagen": self.imagenes[7 - self.intentos]
        }   

        if self.ganador or self.intentos == 0:
            # En caso de que se haya ganado o perdido, ya no se necesita
            # actualizar la palabra.
            self.enviar_respuesta(data)
        
        elif not self.ganador:
            # En otro caso se llenan los espacios en base a la letra usadas.
            palabra = ""
            for letra in self.palabra:
                if letra in self.usadas:
                    palabra += letra
                else:
                    palabra += "_"
                palabra += " "
            
            if palabra.replace(" ", "") == self.palabra:
                # En caso de encontrar todas las letras, se marca como ganado,
                # para no seguir jugando.
                self.mensaje = "Felicitaciones, has gandado!"
                self.ganador = True
                data["msg"] = self.mensaje

                # ======== Para el bonus! =========
                self.end_signal.emit({"gif": self.imagenes["win"]})

            self.palabra_actual = palabra
            data["palabra"] = palabra
        
        self.enviar_respuesta(data)
    
    def enviar_respuesta(self, data):
        # Se envía la información mediante la señal.
        if not self.consola:
            self.respuesta_signal.emit(data)

    def juego_consola(self):
        self.consola = True

        self.nueva_palabra()
        while not self.ganador and self.intentos > 0:
            print(f"\n{'='*40}")
            print(f"Te quedan {self.intentos} intentos.")
            print(f"Has usado las siguientes letras: {self.usadas}")
            print(f"Quedan disponibles las siguientes letras: {self.disponibles}")
            print(f"Llevas descubierto lo siguiente: {self.palabra_actual}")
            print(f"{self.mensaje}\n")

            if not self.ganador or self.intentos == 0:
                letra = "123"
                while len(letra) > 1 or not letra.isalpha():
                    letra = input("Ingresa una letra: ").upper()
                self.check_letra(letra)
        if self.ganador:
            print(f"Ganaste!\n Cerrando aplicanción")
        else:
            print(f"Perdiste :(\n Cerrando aplicanción")

if __name__ == '__main__':
    colgadito = DCColgado()

    colgadito.juego_consola()
