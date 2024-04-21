import socket
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QFileDialog

class FSServer(QWidget):
    
    # Constructor 
    def __init__(self):
        super().__init__()
        self.server = None
        self.client = None
        