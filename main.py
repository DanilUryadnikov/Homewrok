import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random


class round(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ul.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        self.l = []

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_flag(self.qp)
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        d = random.randint(30, 200)
        x = random.randint(50, 600)
        y = random.randint(50, 600)
        self.qp.setBrush(QColor(255, 255, 0))
        self.l.append([x, y, d])
        for i in self.l:
            self.qp.drawEllipse(i[0], i[1], i[2], i[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = round()
    ex.show()
    sys.exit(app.exec())