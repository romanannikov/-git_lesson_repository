import sys
from PyQt5.QtCore import QPoint, Qt, QTime, QTimer
from PyQt5.QtGui import QColor, QPainter, QPolygon, QIcon
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication, QLabel, QPushButton, QWidget,QLCDNumber, QLineEdit, QMessageBox)
from PyQt5 import uic
import os, datetime


class AnalogClock(QWidget):
    hourHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -40)
    ])

    minuteHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -70)
    ])

    hourColor = QColor(120, 0, 127)
    minuteColor = QColor(0, 127, 127, 191)

    def __init__(self, parent=None):
        super(AnalogClock, self).__init__(parent)

        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

        self.setWindowTitle("Analog Clock")
        self.resize(200, 200)

    def paintEvent(self, event):
        side = min(self.width(), self.height())
        time = QTime.currentTime()

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(AnalogClock.hourColor)

        painter.save()
        painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
        painter.drawConvexPolygon(AnalogClock.hourHand)
        painter.restore()

        painter.setPen(AnalogClock.hourColor)

        for i in range(12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(AnalogClock.minuteColor)

        painter.save()
        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawConvexPolygon(AnalogClock.minuteHand)
        painter.restore()

        painter.setPen(AnalogClock.minuteColor)

        for j in range(60):
            if (j % 5) != 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        Calend = QAction(QIcon('Calendar.png'), 'Calendar', self)
        Calend.setShortcut('Ctrl+K')
        Calend.setStatusTip('Calendar')
        Calend.triggered.connect(self.cal)
        self.initUI()

        menubartw = self.menuBar()
        fileMenu2 = menubartw.addMenu('&Tools')        
        fileMenu2.addAction(Calend)
        self.show()

    def initUI(self):
        self.w1 = AnalogClock(self)
        self.w1.move(179, 50)
        self.pushButton.clicked.connect(self.run)

    def cal(self):
        self.h=Calendar()
        self.h.show()

    def run(self):
        try:
            while True:
                if int(self.h.text()) == int(datetime.datetime.now().hour) and int(
                        self.m.text()) == int(datetime.datetime.now().minute):
                    os.system(self.path.text())
                    break
        except Exception:
            pass

class Calendar(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('cal.ui',self)        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = App()
    clock.show()
    sys.exit(app.exec_())
