import sys
from PyQt5.QtCore import QTimer, pyqtSlot
from PyQt5.QtGui import QTextDocument, QPainter, QFontMetrics
from PyQt5.QtWidgets import QLabel, QApplication

class Marquee(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.x = 0
        self.document = None
        self.speed = 0.5
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.translate)
        self.fm = QFontMetrics(self.font())
        self.setFixedSize(200, 20)

    def setText(self, value):
        self.x = 0
        self.document = QTextDocument(self)
        self.document.setPlainText(value)
        self.document.setTextWidth(self.fm.width(value) * 1.06)
        self.document.setUseDesignMetrics(True)

        if self.document.textWidth() > self.width():
            self.timer.start(10)

    @pyqtSlot()
    def translate(self):
        self.x -= self.speed
        if self.x < -self.document.textWidth():
            self.x = self.width()
        self.repaint()

    def paintEvent(self, event):
        if self.document:
            p = QPainter(self)
            p.translate(self.x, 0)
            self.document.drawContents(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Marquee()
    w.setText('Lorem ipsum dolor sit amet, consectetur adipiscing elit...')
    w.show()
    sys.exit(app.exec_())