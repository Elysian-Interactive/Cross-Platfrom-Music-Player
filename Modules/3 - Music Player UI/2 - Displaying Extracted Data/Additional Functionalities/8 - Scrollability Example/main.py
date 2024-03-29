import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QWidget

class MyCustomWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QPushButton('Click me!', self)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Custom Widget in QListWidget Example')
        self.setGeometry(300, 300, 300, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        list_widget = QListWidget()
        layout.addWidget(list_widget)

        # Create custom widgets and add them to QListWidget
        custom_widget1 = MyCustomWidget()
        item1 = QListWidgetItem()
        list_widget.addItem(item1)
        list_widget.setItemWidget(item1, custom_widget1)

        custom_widget2 = MyCustomWidget()
        item2 = QListWidgetItem()
        list_widget.addItem(item2)
        list_widget.setItemWidget(item2, custom_widget2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
