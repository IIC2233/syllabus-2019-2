from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal


class CountChecker(QObject):
    """
    Clase que se encargará de mantener y revisar la cuenta del contador.
    Es parte del back-end del programa, al contener parte de la lógica.
    """

    update_counter_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.counter = 0
        # Se instancia nula la señal a usar para actualizar la ventana
        self.update_window_signal = None

        # Se conecta la señal que recibe de actualizar el contador
        self.update_counter_signal.connect(self.update_counter)

    def update_counter(self):
        """
        Función que actualiza el valor del contador.
        Envía una señal al frontend con el valor actual y
        con un booleano que indica si se superó el número de clics.
        :return: None
        """
        self.counter += 1
        if self.update_window_signal:
            self.update_window_signal.emit(self.counter, self.counter >= 5)


class MenuWindow(QWidget):
    """
    Clase para crear la ventana de menú principal del juego.
    Es parte del front-end del programa, pues solo modifica
    la interfaz gráfica.
    """

    update_window_signal = pyqtSignal(int, bool)

    def __init__(self):
        super().__init__()
        # Se instancia el CountChecker.
        self.count_checker = CountChecker()
        # Se definen los atributos internos de la instancia
        self.instructions_label = None
        self.counter_label = None
        self.main_game_button = None
        self.show_game_signal = None
        # Se inicializa la interfaz y las señales a usar
        self.init_gui()
        self.init_signals()

    def init_gui(self):
        """
        Método que inicializa los componentes visuales de la ventana.
        """
        self.setGeometry(200, 200, 300, 300)
        self.instructions_label = QLabel('Apriete "Jugar" 5 veces para comenzar', self)
        self.counter_label = QLabel('0', self)
        self.main_game_button = QPushButton('Jugar', self)
        vbox = QVBoxLayout()
        vbox.addWidget(self.instructions_label)
        vbox.addWidget(self.counter_label)
        vbox.addWidget(self.main_game_button)
        self.setLayout(vbox)

    def init_signals(self):
        """Método que inicializa las señales a utilizar."""
        # Se conecta la señal que actualiza el contenido de la ventana.
        self.update_window_signal.connect(self.update_window)

        # Se define la señal a utilizar para actualizar el contador.
        self.update_counter_signal = self.count_checker.update_counter_signal
        # Se le entrega al contador la señal para actualizar la interfaz
        self.count_checker.update_window_signal = self.update_window_signal

        # Se conecta el boton con la señal de actualización del contador
        self.main_game_button.clicked.connect(self.update_counter_signal.emit)

    def update_window(self, counter, hide_window):
        """
        Función que actualiza el contenido de la ventana:
        el contador y apertura del juego si corresponde.
        :param counter: int
        :param hide_window: bool
        :return: None
        """
        self.counter_label.setText(str(counter))
        # Si el contador me avisa que es momento de
        # abrir el juego y tengo la señal definida
        if hide_window and self.show_game_signal:
            self.hide()
            self.show_game_signal.emit()
