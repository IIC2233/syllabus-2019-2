from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.Qt import QTest


class Character(QObject):
    """
    Clase que se encargará de manejar los datos internos del personaje.
    Es parte del back-end del programa, al contener parte de la lógica.
    """

    update_character_signal = pyqtSignal(str)

    def __init__(self, x, y):
        super().__init__()
        # Datos iniciales
        self.direction = 'R'
        self._is_ducked = False
        self._x = x
        self._y = y
        self.initial_y = y

        # Se inicializa nula la señal de actualizar la interfaz
        self.update_window_signal = None

        # Se conecta la señal de actualizar datos del personaje
        self.update_character_signal.connect(self.move)

    def update_window_character(self, position='stand'):
        """
        Envía los datos del personaje mediante una señal a la
        interfaz para ser actualizados.
        :param position: str
        :return: None
        """
        if self.update_window_signal:
            self.update_window_signal.emit({
                'x': self.x,
                'y': self.y,
                'direction': self.direction,
                'position': position
            })

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        """
        Actualiza el valor de y del personaje y envía señal de
        actualización a la interfaz.
        :param value: int
        :return: None
        """
        self._y = value
        if self.y < self.initial_y:
            self.update_window_character('jump')
        else:
            self.update_window_character()

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        """
        Chequea que la coordenada x se encuentre dentro los límites
        y envía la señal de actualización a la interfaz.
        :param value: int
        :return: None
        """
        if 0 < value < 780:
            self._x = value
            self.update_window_character('walk')

    @property
    def is_ducked(self):
        return self._is_ducked

    @is_ducked.setter
    def is_ducked(self, value):
        """
        Actualiza si el personaje está agachado o no,
        y envía la señal de actualización a la interfaz.
        :param value: int
        :return: None
        """
        self._is_ducked = value
        if self.is_ducked:
            self.update_window_character('duck')
        else:
            self.update_window_character()

    def move(self, event):
        """
        Función que maneja los eventos de movimiento desde la interfaz.
        :param event: str
        :return: None
        """
        if event == 'R':
            self.direction = 'R'
            self.x += 10
        elif event == 'L':
            self.direction = 'L'
            self.x -= 10
        elif event == 'Jump':
            self.jump()
        elif event == "Duck" and not self.is_ducked:
            self.is_ducked = True
        elif event == "Unduck":
            self.is_ducked = False

    def jump(self):
        """
        Función que ejecuta el salto del personaje.
        :return: None
        """
        if self.y == self.initial_y:
            for i in range(10):
                self.y -= i * 5
                QTest.qWait(30)
            for i in range(10):
                self.y += i * 5
                QTest.qWait(30)
