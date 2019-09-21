import sys
from PyQt5.QtWidgets import QApplication
from menu_window import MenuWindow
from game_window import GameWindow


if __name__ == '__main__':
    app = QApplication([])

    menu_window = MenuWindow()
    game_window = GameWindow()

    menu_window.show_game_signal = game_window.show_game_signal

    menu_window.show()
    sys.exit(app.exec_())
