import sys
from os import path
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDesktopWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class GameControl(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        """
        Este método inicializa la interfaz y todos sus widgets.
        """

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint) 
        self.setWindowTitle('GameControl')
        
        
        # Creamos el QLabel que contendrá la imagen y definimos su tamaño
        self.labelA = QLabel(self)
        self.labelA.setGeometry(70, 180, 110, 110)

        self.labelS = QLabel(self)
        self.labelS.setGeometry(190, 180, 110, 110)

        self.labelD = QLabel(self)
        self.labelD.setGeometry(320, 180, 110, 110)

        self.labelW = QLabel(self)
        self.labelW.setGeometry(160, 65, 110, 110)
        
        # Escribimos la ruta al archivo que contiene la imagen.
        
        ruta_imagen_labelA = path.join('sprites_game_control', 'A.png')
        ruta_imagen_labelS = path.join('sprites_game_control', 'S.png')
        ruta_imagen_labelD = path.join('sprites_game_control', 'D.png')
        ruta_imagen_labelW = path.join('sprites_game_control', 'W.png')
        
        # Cargamos la imagen como pixeles y la agregamos al Qlabel
        self.labelA.setPixmap(QPixmap(ruta_imagen_labelA))
        self.labelS.setPixmap(QPixmap(ruta_imagen_labelS))
        self.labelD.setPixmap(QPixmap(ruta_imagen_labelD))
        self.labelW.setPixmap(QPixmap(ruta_imagen_labelW))
       
        # Una vez que fueron agregados
        # todos los elementos a la ventana la
        # desplegamos en pantalla
        self.show()
        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_A:
            self.labelA.setPixmap(QPixmap(path.join("sprites_game_control", "A_pressed.png")))
        if e.key() == Qt.Key_S:
            self.labelS.setPixmap(QPixmap(path.join("sprites_game_control", "S_pressed.png")))
        if e.key() == Qt.Key_D:
            self.labelD.setPixmap(QPixmap(path.join("sprites_game_control", "D_pressed.png")))
        if e.key() == Qt.Key_W:
            self.labelW.setPixmap(QPixmap(path.join("sprites_game_control", "W_pressed.png")))
            

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_A:
            self.labelA.setPixmap(QPixmap(path.join("sprites_game_control", "A.png")))
        if e.key() == Qt.Key_S:
            self.labelS.setPixmap(QPixmap(path.join("sprites_game_control", "S.png")))
        if e.key() == Qt.Key_D:
            self.labelD.setPixmap(QPixmap(path.join("sprites_game_control", "D.png")))
        if e.key() == Qt.Key_W:
            self.labelW.setPixmap(QPixmap(path.join("sprites_game_control", "W.png")))

if __name__ == '__main__':
    app = QApplication([])
    ventana = GameControl()
    sys.exit(app.exec_())