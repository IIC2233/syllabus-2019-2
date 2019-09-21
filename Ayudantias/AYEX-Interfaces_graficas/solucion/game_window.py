from os import path
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt
from character import Character


class GameWindow(QWidget):
    """
    Clase para crear la ventana del juego mismo. Es parte del front-end
    del programa, al solo modificar la interfaz gráfica.
    """

    update_window_signal = pyqtSignal(dict)
    show_game_signal = pyqtSignal()

    # Se almacena en un diccionario las rutas de imágenes del personaje
    sprites_paths = {
        ('stand', 'R'): path.join('..', 'sprite', 'Super MarioR.png'),
        ('stand', 'L'): path.join('..', 'sprite', 'Super MarioL.png'),
        ('jump', 'R'): path.join('..', 'sprite', 'Super Mario - JumpR.png'),
        ('jump', 'L'): path.join('..', 'sprite', 'Super Mario - JumpL.png'),
        ('duck', 'R'): path.join('..', 'sprite', 'Super Mario - DuckR.png'),
        ('duck', 'L'): path.join('..', 'sprite', 'Super Mario - DuckL.png'),
        ('walk', 'R', 1): path.join('..', 'sprite', 'Super Mario - Walk1.png'),
        ('walk', 'R', 2): path.join('..', 'sprite', 'Super Mario - Walk2.png'),
        ('walk', 'R', 3): path.join('..', 'sprite', 'Super Mario - Walk3.png'),
        ('walk', 'L', 1): path.join('..', 'sprite', 'Super Mario - Walk1L.png'),
        ('walk', 'L', 2): path.join('..', 'sprite', 'Super Mario - Walk2L.png'),
        ('walk', 'L', 3): path.join('..', 'sprite', 'Super Mario - Walk3L.png')
    }

    def __init__(self):
        super().__init__()
        # Se instancia el personaje del backend
        self.backend_character = Character(0, 485)
        self._frame = 1
        # Se definen los otros atributos internos de la instancia
        self.background = None
        self.front_character = None
        self.current_sprite = None
        self.update_character_signal = None
        # Se inicializa la interfaz y las señales a usar
        self.init_gui()
        self.init_signals()

    def init_gui(self):
        """
        Método que inicializa los componentes visuales de la ventana.
        """
        self.setGeometry(100, 100, 800, 600)
        # Se setea la imagen de fondo.
        self.background = QLabel(self)
        background_path = path.join('..', 'sprite', 'background.png')
        self.background.setPixmap(QPixmap(background_path))
        # Se crea el personaje en el frontend.
        self.front_character = QLabel(self)
        self.current_sprite = QPixmap(self.sprites_paths[('stand', 'R')])
        self.front_character.setPixmap(self.current_sprite)
        self.front_character.move(0, 485)

    def init_signals(self):
        """
        Método que inicializa las señales a utilizar.
        """
        # Se conecta la señal para abrir esta ventana con el método show
        self.show_game_signal.connect(self.show)
        # Se conecta la señal de actualización con un método
        self.update_window_signal.connect(self.update_window)
        # Define la señal que actualizará el personaje en back-end
        self.update_character_signal = self.backend_character.update_character_signal
        # Se le asigna al back-end la señal para actualizar esta ventana
        self.backend_character.update_window_signal = self.update_window_signal

    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, value):
        """
        Actualiza el estado de animación de la imagen del personaje.
        Solo tiene 3 estados.
        :param value: int
        :return: None
        """
        self._frame = value if value < 3 else 1

    # Diccionario para asociar teclas con la acción del personaje
    key_event_dict = {
        Qt.Key_D: 'R',
        Qt.Key_A: 'L',
        Qt.Key_Space: 'Jump',
        Qt.Key_S: 'Duck'
    }

    def keyPressEvent(self, event):
        """
        Dada la presión de una tecla se llama a esta función. Al
        apretarse una tecla chequeamos si está dentro de las teclas del
        control del juego y de ser así, se envía una señal al backend
        con la acción además de actualizar el sprite.
        :param event: QKeyEvent
        :return: None
        """
        if event.key() in self.key_event_dict:
            action = self.key_event_dict[event.key()]
            self.update_character_signal.emit(action)

    def keyReleaseEvent(self, event):
        """
        Esta función se llama al soltarse una tecla presionada.
        Si la tecla corresponde a S, debemos actualizar el personaje
        para que deje de agacharse.
        :param event: QKeyEvent
        :return: None
        """
        if event.key() == Qt.Key_S:
            self.update_character_signal.emit('Unduck')

    def update_window(self, event):
        """
        Función que recibe un diccionario con la información del
        personaje y las actualiza en el front-end.
        :param event: dict
        :return: None
        """
        direction = event['direction']
        position = event['position']
        if position == 'walk':
            self.frame += 1
            self.current_sprite = QPixmap(self.sprites_paths[(position, direction, self.frame)])
        else:
            self.current_sprite = QPixmap(self.sprites_paths[(position, direction)])
        self.front_character.setPixmap(self.current_sprite)
        self.front_character.move(event['x'], event['y'])
