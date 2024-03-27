# The main aim of this script is to arrange the UI elements in the specific layouts
# 1. Set the Proper Text labels
# 2. Arrange the cover art properly
# 3. Add the buttons along with their icons

import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QLabel,QHBoxLayout
                            ,QGridLayout,QSizePolicy)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        self.setWindowTitle("UI Look Test")
        self.setGeometry(100,100,400,400)
        self.setupLayout()
        
        self.show()
    
    def setupLayout(self):
        # Make a global grid layout
        grid = QGridLayout(self)
        
        # Make a hbox layout to store the different buttons with icons
        h_box = QHBoxLayout(self)
        
        # Creating a QLabel to store the image
        image_label = QLabel(self)
        image_label.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        
        # Creating a size policy and button size for all the button
        but_size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        but_size = QSize(35,35)
        
        # Create the buttons for the icons to be stored
        play_but = QPushButton(self)
        play_but.setIcon(QIcon("Assets/play-button.png"))
        play_but.setIconSize(QSize(60,60))
        play_but.setSizePolicy(but_size_policy)
        play_but.setStyleSheet("background-color : transparent")
        play_but.resize(QSize(60,60))
        
        next_but = QPushButton(self)
        next_but.setIcon(QIcon("Assets/fast-forward.png"))
        next_but.setIconSize(but_size)
        next_but.setSizePolicy(but_size_policy)
        next_but.setStyleSheet("background-color : transparent")
        next_but.resize(but_size)
        
        prev_but = QPushButton(self)
        prev_but.setIcon(QIcon("Assets/Rewind.png"))
        prev_but.setIconSize(but_size)
        prev_but.setSizePolicy(but_size_policy)
        prev_but.setStyleSheet("background-color : transparent")
        prev_but.resize(but_size)
        
        shuffle_but = QPushButton(self)
        shuffle_but.setIcon(QIcon("Assets/shuffle.png"))
        shuffle_but.setIconSize(but_size)
        shuffle_but.setSizePolicy(but_size_policy)
        shuffle_but.setStyleSheet("background-color : transparent")
        shuffle_but.resize(but_size)
        
        repeat_but = QPushButton(self)
        repeat_but.setIcon(QIcon("Assets/repeat.png"))
        repeat_but.setIconSize(QSize(30,30))
        repeat_but.setSizePolicy(but_size_policy)
        repeat_but.setStyleSheet("background-color : transparent")
        repeat_but.resize(QSize(30,30))
        
        volume_but = QPushButton(self)
        volume_but.setIcon(QIcon("Assets/sound.png"))
        volume_but.setIconSize(QSize(30,30))
        volume_but.setSizePolicy(but_size_policy)
        volume_but.setStyleSheet("background-color : transparent")
        volume_but.resize(QSize(30,30))
        
        #options_but = QPushButton(self)
        
        
        # Adding the buttons to the layout
        h_box.addStretch(6)
        h_box.addWidget(shuffle_but)
        h_box.addWidget(prev_but)
        h_box.addWidget(play_but)
        h_box.addWidget(next_but)
        h_box.addWidget(repeat_but)
        h_box.addStretch(4)
        h_box.addWidget(volume_but)
        h_box.addStretch(1)
        
        # Adding this layout to the grid layout
        grid.rowStretch(5)
        grid.columnStretch(5)
        grid.addWidget(image_label,0,0,4,5)
        grid.addLayout(h_box,4,0,1,5)
        
        self.setLayout(grid)
        
    
app = QApplication(sys.argv)
window = Test()
sys.exit(app.exec_())