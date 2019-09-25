from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5 import uic
from frontend_game import MainGame as GameWindow
from gamecontrol2 import GameControl as GameControlWindow

window_name, base_class = uic.loadUiType("ay_04_mainwindow.ui")


class MainWindow(window_name, base_class):
    '''
    Clase que contiene a otros widgets y que los instancia para actuar como ventana principal.
    '''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # conectamos los botones para que ejecuten acciones.
        self.firstButton.clicked.connect(self.game_control)
        self.secondButton.clicked.connect(self.game)
        self.quitButton.clicked.connect(self.exit)
    
    
    def game_control(self):
        '''
        Método para abrir la ventana de game_control.
        '''
        self.close()
        self.game_control_window = GameControlWindow()
        self.game_control_window.show()


    def game(self):
        '''
        Método para abrir la ventana de juego.
        '''
        self.close()
        self.game_window = GameWindow()
        self.game_window.show()

    def keyPressEvent(self, e):
        '''
        Método para mostrar el funcionamiento de keyPressEvent()
        '''
        if e.key() == Qt.Key_E:
            self.close()
        elif e.key() == Qt.Key_G:
            # Enviar al juego
            self.game()
        elif e.key() == Qt.Key_C:
            # Enviar a conceptos
            self.game_control()

    def exit(self):
        '''
        Método para finalizar el programa
        '''
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec_()

