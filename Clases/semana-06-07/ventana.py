import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QLineEdit)


class VentanaNavegador(QWidget):

    enviar_url_signal = pyqtSignal(str)
    volver_url_signal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Avanzada Explorer")
        self.setGeometry(200, 200, 400, 100)

        # Elementos gráficos
        self.label_url = QLabel("URL:", self)
        self.input_url = QLineEdit(self)
        self.boton_volver = QPushButton("Volver", self)
        self.boton_volver.clicked.connect(self.volver_url)
        self.boton_ir_a = QPushButton("Ir a url", self)
        self.boton_ir_a.clicked.connect(self.ir_a_url)

        # Organizacion de botones
        layout_botones = QHBoxLayout()
        layout_botones.addWidget(self.boton_volver)
        layout_botones.addWidget(self.boton_ir_a)

        # Organización principal de elementos
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.label_url)
        layout_principal.addWidget(self.input_url)
        layout_principal.addLayout(layout_botones)
        self.setLayout(layout_principal)

        self.show()

    def actualizar_url(self, url):
        """
        Este método es llamado al emitir la señal navegador.ir_a_url_signal 
        """
        self.label_url.setText(f"URL: {url}")

    def volver_url(self):
        """
        Este método se ejecuta al hacer click en el botón "Volver"
        """
        self.volver_url_signal.emit()

    def ir_a_url(self):
        """
        Este método se ejecuta al hacer click en el botón "Ir a url"
        """
        texto_ingresado = self.input_url.text()
        self.input_url.setText("")  # Limpiamos el QLineEdit
        self.enviar_url_signal.emit(texto_ingresado)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaNavegador()
    sys.exit(app.exec_())
