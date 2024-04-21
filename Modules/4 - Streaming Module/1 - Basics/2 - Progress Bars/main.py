from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QProgressBar
from PyQt5.QtCore import Qt, QTimer
import sys

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setWindowTitle("Progress Bars")
        self.setGeometry(100,100,200,200)
        
        layout = QVBoxLayout()
        
        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        
        start_button = QPushButton('Start',self)
        start_button.clicked.connect(self.start_progress)
        
        layout.addWidget(self.progressbar)
        layout.addWidget(start_button)
        
        self.setLayout(layout)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        
    def start_progress(self):
        self.progressbar.setValue(0)
        self.timer.start(100)
    
    def update_progress(self):
        cur_val = self.progressbar.value()
        if cur_val >= 100:
            self.timer.stop()
        else:
            self.progressbar.setValue(cur_val + 1)
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
