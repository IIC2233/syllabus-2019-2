import sys
from PyQt5.QtWidgets import QApplication
from ventana import VentanaNavegador
from navegador import Navegador


# (Debuggeo en PyQt5)
def hook(type, value, traceback):
    print(type)
    print(traceback)
sys.__excepthook__ = hook

# Se instancia la app
app = QApplication([])

# Se crea el back-end
navegador = Navegador(url_inicial="google.com")

# Se crea el front-end
ventana = VentanaNavegador()
ventana.show()

# Se conectan las señales respectivas
ventana.enviar_url_signal.connect(navegador.ir_a)  # Recibe str
ventana.volver_url_signal.connect(navegador.volver)  # No recibe args
navegador.ir_a_url_signal.connect(ventana.actualizar_url)  # Recibe str

# Se inicia el navegador en la página de inicio
navegador.ir_a_url_signal.emit(navegador.mostrar_pagina_actual())

sys.exit(app.exec())
