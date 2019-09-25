# Acá va lo relacionado con la GUI.
import sys
from os.path import join
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QObject, pyqtSignal, Qt, pyqtSlot, QRect
from PyQt5.QtMultimedia import QSound
from backend_game import Character
from random import randint
from threading import Lock


class MainGame(QWidget):

    move_character_signal = pyqtSignal(str)
    part_adder_lock = Lock()

    def __init__(self):
        super().__init__()
        self.directions = {Qt.Key_D: 'R', Qt.Key_A: 'L',
                           Qt.Key_W: 'U', Qt.Key_S: 'D'}

        self.libraries = dict()
        self.front_entities = []
        self.setGeometry(100, 100, 512, 512)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(join('sprites_game', 'background.bmp')).scaledToHeight(512))

        front_character = QLabel(self)
        front_character.setGeometry(QRect(300, 300, 30, 30))
        front_character.setPixmap(QPixmap(join('sprites_game', 'snake_head.png')))
        self.front_entities.append(front_character)

        self.backend_character = Character(self, 300, 300)
        self.move_character_signal.connect(self.backend_character.update_dir)

        self.music = QSound(join("sounds", "snake_audio.wav"))
        self.audio_eat = QSound(join("sounds", "snake_eat.wav"))
        self.music.setLoops(-1)
        self.music.play()

    def keyPressEvent(self, e):
        key = e.key()
        if key in self.directions:
            self.move_character_signal.emit(self.directions[key])

    @pyqtSlot(dict)
    def update_from_backend(self, event):
        status = event['status']
        if status == 'move':
            self.move_snake_part(event)
            
        elif status == 'new_library':
            self.create_library(event)
            
        elif status == 'ate':
            self.eat_library(event)

    def move_snake_part(self, event):
        part = event['part']
        if part == len(self.front_entities):
            # Si la parte no existe, agregamos una
            with self.part_adder_lock:
                body_part = QLabel('', self)
                body_part.setGeometry(QRect(event['x'], event['y'], 30, 30))
                body_part.setPixmap(QPixmap(join('sprites_game', 'snake_body.png')))
                body_part.show()
                self.front_entities.append(body_part)
        elif part > len(self.front_entities):
            # si es que se agregaron dos partes instantáneamente,
            # retornamos para que después se agregue la otra
            return

        part_to_move = self.front_entities[part]

        part_to_move.move(event['x'], event['y'])

    def create_library(self, event):
        library = QLabel('', self)
        library.setGeometry(event['location'])
        library.setPixmap(QPixmap(join('sprites_game', 'library.png')))
        self.libraries[event['coordenates']] = library
        library.show()

    def eat_library(self, event):
        self.audio_eat.play()
        library = self.libraries[event['coordenates']]
        library.hide()
        library.deleteLater()
        del self.libraries[event['coordenates']]


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])
    form = MainGame()
    form.show()
    sys.exit(app.exec_())
