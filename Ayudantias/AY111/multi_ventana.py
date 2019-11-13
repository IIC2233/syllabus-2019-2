import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QLCDNumber, QMainWindow, QAction
from PyQt5.QtCore import QThread
import sys
from PyQt5.Qt import QTest
import random


class Instancia(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.labels = []
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.setStyleSheet(f"background-color: rgb({r},{g},{b})")
        x = random.randint(0, 1800)
        y = random.randint(0, 1000)
        self.setGeometry(x, y, x, y)
        self.theadd = threading.Thread(target=self.run)
        self.theadd.start()

    def run(self):
        QTest.qWait(2000)
        while True:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.setStyleSheet(f"background-color: rgb({r},{g},{b})")
            QTest.qWait(20)


my_threads = []
app = QApplication([])
for i in range(100):
    s = Instancia()
    s.show()

    my_threads.append(s)

sys.exit(app.exec_())
