import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget, QLabel, QPushButton, QVBoxLayout
 
class Widget1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        label = QLabel("Welcome to Widget 1!")
        layout.addWidget(label)
        button = QPushButton("Switch to Widget 2")
        button.clicked.connect(self.switch_widget)
        layout.addWidget(button)
        self.setLayout(layout)
 
    def switch_widget(self):
        stacked_widget.setCurrentIndex(1)
 
 
class Widget2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        label = QLabel("Welcome to Widget 2!")
        layout.addWidget(label)
        button = QPushButton("Switch to Widget 1")
        button.clicked.connect(self.switch_widget)
        layout.addWidget(button)
        self.setLayout(layout)
 
    def switch_widget(self):
        stacked_widget.setCurrentIndex(0)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
 
    # Create the QStackedWidget and add the two widgets to it
    stacked_widget = QStackedWidget()
    widget1 = Widget1()
    widget2 = Widget2()
    stacked_widget.addWidget(widget1)
    stacked_widget.addWidget(widget2)
 
    # Show the first widget
    stacked_widget.setCurrentIndex(0)
    stacked_widget.show()
 
    sys.exit(app.exec_())