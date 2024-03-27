import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MyGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a QGraphicsScene
        scene = QGraphicsScene()
        self.setScene(scene)

        # Create a QLabel widget
        label = QLabel("Label")
        pixmap = QPixmap("image.png")
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

        # Create a QPushButton widget
        button = QPushButton("Button")

        # Create QGraphicsProxyWidget for each widget
        label_proxy = QGraphicsProxyWidget()
        label_proxy.setWidget(label)

        button_proxy = QGraphicsProxyWidget()
        button_proxy.setWidget(button)

        # Add widgets to the scene and set their positions
        scene.addItem(label_proxy)
        label_proxy.setPos(50, 50)  # Position of the label
        scene.addItem(button_proxy)
        button_proxy.setPos(100, 100)  # Position of the button

        # Set up the view
        self.setWindowTitle("Overlaying Widgets Example")
        self.setGeometry(100, 100, 400, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MyGraphicsView()
    sys.exit(app.exec_())
