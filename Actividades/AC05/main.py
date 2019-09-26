from PyQt5.QtWidgets import QApplication
from Ventanas import VentanaJuego
from DCColgado import DCColgado
import sys


def hook(type, value, traceback):
    print(type)
    print(traceback)
sys.__excepthook__ = hook

# Se instancia la app
app = QApplication(sys.argv)

# Se crea el Front-end
ventana = VentanaJuego()
ventana.show()

# Se crea el Back-end
DCC_51 = DCColgado()

# Se conectan las señales de front-end con el back-end.
ventana.enviar_letra_signal.connect(DCC_51.check_info)
ventana.reiniciar_signal.connect(DCC_51.nueva_palabra)


# ===== Debes conectar esta señal con el metodo respectivo del front-end ======
# DCC_51.respuesta_signal.connect()


# Se inicia una partida.
ventana.reiniciar_signal.emit()
sys.exit(app.exec())
