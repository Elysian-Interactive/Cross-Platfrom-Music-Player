# This file will deal with the working of the QSlider

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QSlider,QVBoxLayout,QMainWindow,QLabel
from PyQt5.QtCore import Qt

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setWindowTitle("Slider Test")
        self.setGeometry(100,100,400,400)
        self.setupTest()
        
        self.show()
    
    def setupTest(self):
    
        v_slider = QSlider(Qt.Vertical,self)
        v_slider.setFocusPolicy(Qt.StrongFocus)
        v_slider.setMaximum(100)
        #v_slider.hide() # Hides the slider
        
        h_slider = QSlider(Qt.Horizontal,self)
        h_slider.setMaximum(100)
        
        v_box = QVBoxLayout(self)
        v_box.addWidget(v_slider)
        v_box.addWidget(h_slider)
        
        self.setLayout(v_box)

def main():
    app = QApplication(sys.argv)
    window = Test()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
        
        