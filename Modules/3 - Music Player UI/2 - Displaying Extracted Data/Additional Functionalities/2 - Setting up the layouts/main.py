# The main aim of this script is to arrange the UI elements in the specific layouts
# 1. Set the Proper Text labels
# 2. Arrange the cover art properly
# 3. Add the buttons along with their icons

import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QHBoxLayout,QGridLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    
    def initializeUI(self):
        self.setWindowTitle("UI Look Test")
        