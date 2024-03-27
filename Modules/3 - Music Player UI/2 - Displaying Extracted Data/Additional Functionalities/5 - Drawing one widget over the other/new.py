import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsWidget, QPushButton, QLabel, QGraphicsLinearLayout, QGraphicsProxyWidget
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

        # Create a QGraphicsWidget to hold the layouts
        widget = QGraphicsWidget()
        layout = QGraphicsLinearLayout(Qt.Vertical)
        widget.setLayout(layout)

        # Create widgets
        label = QLabel("Label")
        pixmap = QPixmap("image.png")
        label.setPixmap(pixmap)
        button = QPushButton("Button")
        
        # Create QGraphicsProxyWidget for each widget
        label_proxy = QGraphicsProxyWidget()
        label_proxy.setWidget(label)

        button_proxy = QGraphicsProxyWidget()
        button_proxy.setWidget(button)

        # Add widgets to the layout
        layout.addItem(label_proxy)
        layout.addItem(button_proxy)

        # Add the widget with layout to the scene
        scene.addItem(widget)

        # Set position for the widget
        widget.setPos(50, 50)

        # Set up the view
        self.setWindowTitle("Layouts in QGraphicsView Example")
        self.setGeometry(100, 100, 400, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MyGraphicsView()
    sys.exit(app.exec_())
