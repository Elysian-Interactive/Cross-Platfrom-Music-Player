# The main aim of this script is to arrange the UI elements in the specific layouts
# 1. Set the Proper Text labels
# 2. Arrange the cover art properly
# 3. Add the buttons along with their icons

# Pending Functionality : add QToolTip to all the buttons

import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QLabel,QHBoxLayout
                            ,QVBoxLayout,QGridLayout,QSizePolicy,QSlider,QToolTip)
from PyQt5.QtGui import QIcon,QPixmap,QFont
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
        # Creating the tool tip to display info about the buttons
        QToolTip.setFont(QFont('Helvetica',10))
    
        # Make a global grid layout
        grid = QGridLayout(self)
        
        # Layout for handling the image
        image_layout = QHBoxLayout(self)
        
        # Make a hbox layout to store the different buttons with icons
        playback_layout = QHBoxLayout(self)
        
        # Make a hbox layout for storing the slider and corresponding labels
        info_layout = QHBoxLayout(self)
        
        # Make a hbox layout for storing the volume slider
        vol_layout = QHBoxLayout(self)
        
        # Creating a QLabel to store the image
        image_label = QLabel(self)
        image_label.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        pixmap = QPixmap("God of War.jpg")
        image_label.setPixmap(pixmap)
        
        # Creating a size policy and button size for all the button
        but_size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        but_size = QSize(35,35)
        
        # Creating a QWidget to display information about the song and artist
        # Additional features : constratint the horizontal width
        song_info = QWidget(self)
        song_info.setMinimumSize(150,80)
        song_info.setMaximumSize(200,80)
        song_info.setStyleSheet("QWidget#window{"
                                "border: 2px solid rgba(0, 0, 0, 0.2);" 
                                "}")
        
        song_name = QLabel("God Of War",song_info)
        song_name.setFont(QFont('Ariel',20))
        
        artist_name = QLabel("Bear McCreary",song_info)
        artist_name.setFont(QFont('Ariel',12))
        
        song_info_layout = QVBoxLayout(song_info)
        song_info_layout.addStretch()
        song_info_layout.addWidget(song_name)
        song_info_layout.addWidget(artist_name)
        song_info_layout.addStretch()
        
        song_info.setLayout(song_info_layout)
        song_info.show()
        
        # Create the buttons for the icons to be stored
        play_but = QPushButton(self)
        play_but.setIcon(QIcon("Assets/play-button.png"))
        play_but.setIconSize(QSize(60,60))
        play_but.setSizePolicy(but_size_policy)
        play_but.setStyleSheet("background-color : transparent")
        play_but.resize(QSize(60,60))
        play_but.setToolTip("Play/Pause Song")
        
        next_but = QPushButton(self)
        next_but.setIcon(QIcon("Assets/fast-forward.png"))
        next_but.setIconSize(but_size)
        next_but.setSizePolicy(but_size_policy)
        next_but.setStyleSheet("background-color : transparent")
        next_but.resize(but_size)
        next_but.setToolTip("Next Song")
        
        prev_but = QPushButton(self)
        prev_but.setIcon(QIcon("Assets/Rewind.png"))
        prev_but.setIconSize(but_size)
        prev_but.setSizePolicy(but_size_policy)
        prev_but.setStyleSheet("background-color : transparent")
        prev_but.resize(but_size)
        prev_but.setToolTip("Previous Song")
        
        shuffle_but = QPushButton(self)
        shuffle_but.setIcon(QIcon("Assets/shuffle.png"))
        shuffle_but.setIconSize(but_size)
        shuffle_but.setSizePolicy(but_size_policy)
        shuffle_but.setStyleSheet("background-color : transparent")
        shuffle_but.resize(but_size)
        shuffle_but.setToolTip("Shuffle")
        
        repeat_but = QPushButton(self)
        repeat_but.setIcon(QIcon("Assets/repeat.png"))
        repeat_but.setIconSize(QSize(30,30))
        repeat_but.setSizePolicy(but_size_policy)
        repeat_but.setStyleSheet("background-color : transparent")
        repeat_but.resize(QSize(30,30))
        repeat_but.setToolTip("Repeat")
        
        queue_but = QPushButton(self)
        queue_but.setIcon(QIcon("Assets/queue.png"))
        queue_but.setIconSize(QSize(30,30))
        queue_but.setSizePolicy(but_size_policy)
        queue_but.setStyleSheet("background-color : transparent")
        queue_but.resize(QSize(30,30))
        queue_but.setToolTip("Playing Queue")
        
        # Creating widgets to be added in the info section
        current_time = QLabel("00:00",self)
        end_time = QLabel("00:00",self)
        time_slider = QSlider(Qt.Horizontal,self)
        
        # Creating widgets to be added in the volume layout
        
        vol_widget = QWidget(self)
        # Volume Button
        min_vol_but = QPushButton(vol_widget)
        min_vol_but.setIcon(QIcon("Assets/sound.png"))
        min_vol_but.setIconSize(QSize(20,20))
        min_vol_but.setSizePolicy(but_size_policy)
        min_vol_but.setStyleSheet("background-color : transparent")
        min_vol_but.resize(QSize(20,20))
        min_vol_but.setToolTip("Mute")
        
        # Volume Slider
        vol_slider = QSlider(Qt.Horizontal,vol_widget)
        vol_slider.setRange(0,100)
        vol_slider.setMaximumWidth(150)
        vol_slider.setMinimumWidth(50)
        
        # Creating a layout to store them
        vol_h_layout = QHBoxLayout(vol_widget)
        vol_h_layout.addWidget(min_vol_but)
        vol_h_layout.addWidget(vol_slider)
        
        vol_widget.setLayout(vol_h_layout)
        vol_widget.show()
        
        # Image Layout
        image_layout.addStretch()
        image_layout.addWidget(image_label)
        image_layout.addStretch()
       
        # Adding the items to the info layout
        info_layout.addWidget(current_time)
        info_layout.addWidget(time_slider)
        info_layout.addWidget(end_time)
       
        # Adding the buttons to the layout
        playback_layout.addWidget(song_info)
        playback_layout.addStretch(5)
        playback_layout.addWidget(shuffle_but)
        playback_layout.addWidget(prev_but)
        playback_layout.addWidget(play_but)
        playback_layout.addWidget(next_but)
        playback_layout.addWidget(repeat_but)
        playback_layout.addStretch(5)
        playback_layout.addWidget(vol_widget)
        playback_layout.addWidget(queue_but)
        playback_layout.addStretch()
        
        # Adding this layout to the grid layout
        grid.rowStretch(20)
        grid.columnStretch(5)
        grid.addLayout(image_layout,0,0,15,5)
        grid.addLayout(info_layout,15,0,1,5)
        grid.addLayout(vol_layout,16,0,1,5)
        grid.addLayout(playback_layout,17,0,2,5)
        
        self.setLayout(grid)
        
    
app = QApplication(sys.argv)
window = Test()
sys.exit(app.exec_())