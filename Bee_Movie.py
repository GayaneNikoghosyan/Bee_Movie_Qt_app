from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDesktopWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5 import QtCore
import random


class Bee(QWidget):
    def __init__(self):
        super().__init__()

        # Get Screen, Window and Movable area - Width and Height
        self.screen_width = QDesktopWidget().availableGeometry().width()
        self.screen_height = QDesktopWidget().availableGeometry().height()
        self.width = min(self.screen_width, self.screen_height) // 4
        self.height = self.width
        self.max_width = self.screen_width - self.width
        self.max_height = self.screen_height - self.height

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(self.screen_width // 2 - self.width // 2, self.screen_height // 2 - self.height // 2,
                         self.width, self.height)

        # Setting a label in the main window.
        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.label.installEventFilter(self)

        # Setting a GIF in the label.
        self.movie = QMovie("bee.gif")
        self.movie.setScaledSize(QSize().scaled(100, 100, Qt.KeepAspectRatio))
        self.label.setMovie(self.movie)
        self.movie.start()

        # Create BeeAnimation
        self.label.resize(100, 100)
        self.anim = QPropertyAnimation(self, b"pos")
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        self.anim.setEndValue(QPoint(random.randint(0, self.max_width), random.randint(0, self.max_height)))

        self.anim.setDuration(2000)
        self.anim.start()

        # Modify label Mouse Enter Event
        self.label.installEventFilter(self)

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            self.label.resize(100, 100)
            self.anim = QPropertyAnimation(self, b"pos")
            self.anim.setEasingCurve(QEasingCurve.OutBounce)
            self.anim.setEndValue(QPoint(random.randint(0, self.max_width), random.randint(0, self.max_height)))

            self.anim.setDuration(3000)
            self.anim.start()

        return False


if __name__ == '__main__':
    app = QApplication([])
    win = Bee()
    win.show()
    app.exec()