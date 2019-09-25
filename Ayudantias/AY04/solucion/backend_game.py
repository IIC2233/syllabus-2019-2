from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread, QRect
from PyQt5.Qt import QTest 
from collections import deque
from random import randint
from threading import Lock


class Libraries(QThread):
    to_snake_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        # se crean las casillas del tablero
        row = ['']*17
        columns = []
        for i in range(17):
            new_row = row[:]
            columns.append(new_row)
        self.columns = columns

    def run(self):
        while True:
            self.add_fruit()
            QTest.qWait(3700)

    def add_fruit(self):
        """
        Funcion que crea una fruta y manda una señal para que se haga visible en el frontend
        :return: None
        """
        x = randint(0, 16)
        y = randint(0, 16)

        if self.columns[y][x]:
            """
            Si ya hay una fruta en la nueva casilla,
            la operacion se cancela
            """
            return
        rect = QRect(1 + 30 * x, 1 + 30 * y, 30, 30)
        self.columns[y][x] = rect
        self.to_snake_signal.emit({'status': 'new_library', 'coordenates': (x, y), 'location': rect})
        
    @pyqtSlot(tuple)
    def check_snake(self, location):
        """
        funcion que recibe la nueva ubicacion de la serpiente,
        y que revisa si esta está en una fruta para comerla
        :param location: tuple
        :return: None
        """
        snake_x, snake_y = location
        bottom_snake_x = snake_x // 30
        top_snake_x = (snake_x // 30) + 1

        bottom_snake_y = snake_y // 30
        top_snake_y = (snake_y // 30) + 1
        
        for x in [bottom_snake_x, top_snake_x]:
            for y in [bottom_snake_y, top_snake_y]:
                if x > 16 or y > 16 or x < 0 or y < 0:
                    """
                    Es decir, si la posición no es válida,
                    probamos otra casilla
                    """
                    continue
                if self.columns[y][x]:
                    self.to_snake_signal.emit({'status': 'ate', 'coordenates': (x, y)})
                    self.columns[y][x] = None


class BodyTimer(QThread):
    """
    Clase que se encarga de actualizar las partes de la serpiente para el frontend
    """

    snake_signal = pyqtSignal(dict)

    def __init__(self, max_parts, x, y):
        super().__init__()
        self.x, self.y = x, y
        self.current_body_part = 0
        self.max_body_parts = max_parts

    def run(self):

        while (self.max_body_parts + 1) * 10 >= self.current_body_part:
            info = {'x': self.x, 'y': self.y,
                    'part': self.current_body_part}

            self.snake_signal.emit(info)

            self.current_body_part += 1

            QTest.qWait(450)


class Character(QThread):

    update_frontend_signal = pyqtSignal(dict)
    update_library = pyqtSignal(tuple)
    eat_lock = Lock()

    def __init__(self, parent, x, y):
        super().__init__()
        self.length = 0
        self._x = x
        self._y = y
        self.direction = None
        self.move_duration = 150

        self.libraries = Libraries()
        self.libraries.to_snake_signal.connect(self.recieve_from_library)
        self.update_library.connect(self.libraries.check_snake)

        self.update_frontend_signal.connect(parent.update_from_backend)

    def run(self):
        self.libraries.start()
        while True:
            thread = BodyTimer(self.length, self.x, self.y)
            thread.snake_signal.connect(self.update_front)
            thread.start()
            self.move()
            QTest.qWait(self.move_duration)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if 0 <= value < 512 - 30:
            self._y = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if 0 <= value < 512 - 30:
            self._x = value

    @pyqtSlot(dict)
    def update_front(self, info):
        """
        :param info: dict
        :return:
        recibe atributos del BodyTimer
        """
        x = info['x']
        y = info['y']
        body_part = info['part']
        if body_part == 0:  # es decir, la cabeza de la serpiente
            """
            Se actualiza la posición al encargado de librerías
            para saber si la serpiente se comió una librería o no
            """
            self.update_library.emit((x, y))
        
        if body_part > self.length:
            """
            Si la parte de la serpiente no corresponde a una que ya tenga,
            no se actualiza el frontend
            """
            return
        self.update_frontend_signal.emit({'status': 'move', 'x': x, 'y': y, 'dir': self.direction,
                                          'part': body_part})

    @pyqtSlot(str)
    def update_dir(self, event):
        """
        funcion que actualiza la direccion de la serpiente
        Recibe del frontend la direccion
        :param event: str
        :return:
        """
        if self.direction is None:
            self.start()
        self.direction = event

    @pyqtSlot(dict)
    def recieve_from_library(self, event):
        """
        funcion que recibe de Libraries
        Avisa si la serpiente se comio una libreria o aparecio una.
        Ademas avisa al frontend
        :param event: dict
        :return:
        """
        status = event['status']
        if status == 'ate':
            with self.eat_lock:
                self.length += 1
        self.update_frontend_signal.emit(event)

    def move(self):

        if self.direction == 'R':
            self.x += 10

        elif self.direction == 'L':
            self.x -= 10

        elif self.direction == 'U':
            self.y -= 10

        elif self.direction == 'D':
            self.y += 10
