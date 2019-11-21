from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QPushButton, QLabel, QApplication,
                             QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QGroupBox)

import sys
import re


from threading import Event, Lock

class Interfaz(QWidget):

    senal_a_backend = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 100, 800, 400)
        self.setWindowTitle("Japonizador")

        # layout general
        layout = QVBoxLayout()

        # layout arriba
        layout_arriba = QHBoxLayout()
        layout_arriba.setSpacing(0)
        self.boton = QPushButton('&Enviar Palabra', self)
        self.boton.setEnabled(False)
        self.boton.resize(self.boton.sizeHint())
        self.boton.clicked.connect(self.manejar_boton)
        layout_arriba.addWidget(self.boton)


        self.edit = QLineEdit('', self)
        # Para que se edite el texto correctamente, se conecta a una funcion
        # que se activará con cada edicion del QLineEdit
        self.edit.textEdited.connect(self.editar_texto)
        layout_arriba.addWidget(self.edit)

        # vision del ultimo request del usuario
        req_usuario = QGroupBox('Tu ultima consulta')
        req_usuario_layout = QVBoxLayout()
        req_usuario_layout.setSpacing(0)
        self.usuario_palabra_original = QLabel("Palabra:", self)
        req_usuario_layout.addWidget(self.usuario_palabra_original)
        self.usuario_palabra_fonetica = QLabel("Japonizado:", self)
        req_usuario_layout.addWidget(self.usuario_palabra_fonetica)
        self.usuario_palabra_en_japones = QLabel("En japones:", self)
        req_usuario_layout.addWidget(self.usuario_palabra_en_japones)
        req_usuario.setLayout(req_usuario_layout)

        # vision del ultimo request al servidor
        req_todos = QGroupBox('Ultima consulta al servidor')
        req_todos_layout = QVBoxLayout()
        req_todos_layout.setSpacing(0)
        self.todos_palabra_original = QLabel("Palabra:", self)
        req_todos_layout.addWidget(self.todos_palabra_original)
        self.todos_palabra_fonetica = QLabel("Japonizado:", self)
        req_todos_layout.addWidget(self.todos_palabra_fonetica)
        self.todos_palabra_en_japones = QLabel("En japones:", self)
        req_todos_layout.addWidget(self.todos_palabra_en_japones)
        req_todos.setLayout(req_todos_layout)

        layout.addLayout(layout_arriba)
        layout.addStretch(1)
        layout.addWidget(req_usuario)
        layout.addStretch(1)
        layout.addWidget(req_todos)
        self.setLayout(layout)

        self.show()

    def editar_texto(self):
        self.edit.setText(re.sub(r"[#*<>\'&]", '', self.edit.text()))
        if len(self.edit.text()) == 0:  # Si no hay texto no se envía
            self.boton.setEnabled(False)
        else:
            self.boton.setEnabled(True)

    def manejar_boton(self):
        """
        Este método envía la palabra actualmente contenida
        en el QLineEdit a la clase Cliente
        :return:
        """
        self.senal_a_backend.emit(self.edit.text())

    def desplegar_resultado(self, mensaje):
        """
        Este metodo actualiza la informacion que se ve en pantalla
        :param mensaje: dict, posee la informacion para actualizar
        :return:
        """
        original = mensaje["original"]
        fonetica = mensaje["fonetica"]
        traducida = mensaje["traducida"]
        if mensaje["propio"]:  # Significa que este usuario envio la request
            self.usuario_palabra_original.setText(f"Palabra: {original}")
            self.usuario_palabra_fonetica.setText(f"Japonizado: {fonetica}")
            self.usuario_palabra_en_japones.setText(f"En japones: {traducida}")

        else:  # Es decir, que se actualiza el campo de la ultima consulta en general al servidor
            self.todos_palabra_original.setText(f"Palabra: {original}")
            self.todos_palabra_fonetica.setText(f"Japonizado: {fonetica}")
            self.todos_palabra_en_japones.setText(f"En japones: {traducida}")



if __name__ == '__main__':
    app = QApplication([])

    def hook(type, value, traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    front = Interfaz()

    sys.exit(app.exec_())