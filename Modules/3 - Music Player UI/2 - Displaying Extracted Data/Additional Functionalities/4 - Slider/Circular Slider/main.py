import sys
from PyQt5.QtWidgets import QApplication, QSlider, QMainWindow
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter, QColor, QBrush

class CircularSlider(QSlider):
    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super().__init__(orientation, parent)

        self.sliderHandleRadius = 10
        self.sliderHandleColor = QColor(0, 0, 255)  # Blue color for the handle

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the slider track
        self.drawSliderTrack(painter)

        # Draw the circular slider handle
        self.drawCircularHandle(painter)

    def drawSliderTrack(self, painter):
        trackRect = self.getSliderHandleRect()
        trackColor = QColor(200, 200, 200)  # Gray color for the track
        trackBrush = QBrush(trackColor)
        painter.setBrush(trackBrush)
        painter.drawRect(trackRect)

    def drawCircularHandle(self, painter):
        handleRect = self.getSliderHandleRect()
        handleColor = self.sliderHandleColor
        handleBrush = QBrush(handleColor)
        painter.setBrush(handleBrush)
        painter.drawEllipse(handleRect)

    def getSliderHandleRect(self):
        sliderRange = self.maximum() - self.minimum()
        sliderLength = self.width() if self.orientation() == Qt.Horizontal else self.height()
        sliderRatio = (self.value() - self.minimum()) / sliderRange

        if self.orientation() == Qt.Horizontal:
            handleX = int(sliderRatio * (self.width() - self.sliderHandleRadius * 2))
            handleRect = QRectF(handleX, 0, self.sliderHandleRadius * 2, self.height())
        else:
            handleY = int((1.0 - sliderRatio) * (self.height() - self.sliderHandleRadius * 2))
            handleRect = QRectF(0, handleY, self.width(), self.sliderHandleRadius * 2)

        return handleRect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Circular Slider Example')
        self.setGeometry(300, 300, 300, 200)

        self.slider = CircularSlider(Qt.Horizontal, self)
        self.slider.setGeometry(50, 50, 200, 20)
        self.slider.setRange(0, 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
