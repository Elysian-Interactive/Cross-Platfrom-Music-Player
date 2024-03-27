import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QToolTip)
from PyQt5.QtGui import QFont

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setWindowTitle("ToolTip Example")
        self.setGeometry(100,100,200,200)
        self.setupTest()
        
        self.show()
    
    def setupTest(self):
        QToolTip.setFont(QFont('Helvetica',10))
        
        button = QPushButton("Hover over to find out",self)
        button.setToolTip("This is a button")
        
app = QApplication(sys.argv)
window = Test()
sys.exit(app.exec_())
        