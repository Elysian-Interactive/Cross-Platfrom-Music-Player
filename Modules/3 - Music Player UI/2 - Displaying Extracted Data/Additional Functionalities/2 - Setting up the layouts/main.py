# The main aim of this script is to arrange the UI elements in the specific layouts
# 1. Set the Proper Text labels
# 2. Arrange the cover art properly
# 3. Add the buttons along with their icons

# Pending Functionality : add QToolTip to all the buttons

import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QLabel,QHBoxLayout
                            ,QVBoxLayout,QGridLayout,QSizePolicy,QSlider,QToolTip
                            ,QStackedWidget)
from PyQt5.QtGui import QIcon,QPixmap,QFont
from PyQt5.QtCore import Qt, QSize, QTimer

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        self.setWindowTitle("UI Look Test")
        self.setGeometry(100,100,400,400)
        self.setupUI()
        
        self.show()
    
    def setupUI(self):
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
        
        # Creating a Stacked Widget for switching between the playlist view and
        # the image view
        
        # Creating a QLabel to store the image
        self.image_widget = QWidget()
        self.image_label = QLabel(self)
        self.image_label.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        pixmap = QPixmap("Assets/musical.png")
        pixmap = pixmap.scaled(500,500)
        self.image_label.setPixmap(pixmap)
        
        # Creating a Playlist view which would contain certain buttons for adding song
        self.playing_queue_widget = QWidget()
        # Create labels and buttons
        self.pq_title = QLabel("Playing Queue",self.playing_queue_widget)
        self.pq_title.setFont(QFont('Ariel',20))
        
        self.add_song_but = QPushButton("Add Song(s)",self.playing_queue_widget)
        self.add_folder_but = QPushButton("Add Folder")
        self.clear_song_but = QPushButton(self.playing_queue_widget)
        
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
        
        self.song_name = QLabel("Unknown    ",song_info)
        self.song_name.setFont(QFont('Ariel',20))
        
        self.artist_name = QLabel("Unknown",song_info)
        self.artist_name.setFont(QFont('Ariel',12))
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animateText)
        self.timer.start(1000)  # Milliseconds
        
        song_info_layout = QVBoxLayout(song_info)
        song_info_layout.addStretch()
        song_info_layout.addWidget(self.song_name)
        song_info_layout.addWidget(self.artist_name)
        song_info_layout.addStretch()
        
        song_info.setLayout(song_info_layout)
        song_info.show()
        
        # Create the buttons for the icons to be stored
        self.play_but = QPushButton(self)
        self.play_but.setIcon(QIcon("Assets/play-button.png"))
        self.play_but.setIconSize(QSize(60,60))
        self.play_but.setSizePolicy(but_size_policy)
        self.play_but.setStyleSheet("background-color : transparent")
        self.play_but.resize(QSize(60,60))
        self.play_but.setToolTip("Play/Pause Song")
        
        self.next_but = QPushButton(self)
        self.next_but.setIcon(QIcon("Assets/fast-forward.png"))
        self.next_but.setIconSize(but_size)
        self.next_but.setSizePolicy(but_size_policy)
        self.next_but.setStyleSheet("background-color : transparent")
        self.next_but.resize(but_size)
        self.next_but.setToolTip("Next Song")
        
        self.prev_but = QPushButton(self)
        self.prev_but.setIcon(QIcon("Assets/Rewind.png"))
        self.prev_but.setIconSize(but_size)
        self.prev_but.setSizePolicy(but_size_policy)
        self.prev_but.setStyleSheet("background-color : transparent")
        self.prev_but.resize(but_size)
        self.prev_but.setToolTip("Previous Song")
        
        self.shuffle_but = QPushButton(self)
        self.shuffle_but.setIcon(QIcon("Assets/shuffle.png"))
        self.shuffle_but.setIconSize(but_size)
        self.shuffle_but.setSizePolicy(but_size_policy)
        self.shuffle_but.setStyleSheet("background-color : transparent")
        self.shuffle_but.resize(but_size)
        self.shuffle_but.setToolTip("Shuffle")
        
        self.repeat_but = QPushButton(self)
        self.repeat_but.setIcon(QIcon("Assets/repeat.png"))
        self.repeat_but.setIconSize(QSize(30,30))
        self.repeat_but.setSizePolicy(but_size_policy)
        self.repeat_but.setStyleSheet("background-color : transparent")
        self.repeat_but.resize(QSize(30,30))
        self.repeat_but.setToolTip("Repeat")
        
        self.queue_but = QPushButton(self)
        self.queue_but.setIcon(QIcon("Assets/queue.png"))
        self.queue_but.setIconSize(QSize(30,30))
        self.queue_but.setSizePolicy(but_size_policy)
        self.queue_but.setStyleSheet("background-color : transparent")
        self.queue_but.resize(QSize(30,30))
        self.queue_but.setToolTip("Playing Queue")
        
        # Creating widgets to be added in the info section
        self.current_time = QLabel("00:00",self)
        self.end_time = QLabel(" 00:00",self)
        self.time_slider = QSlider(Qt.Horizontal,self)
        
        # Creating widgets to be added in the volume layout
        
        vol_widget = QWidget(self)
        # Volume Button
        self.min_vol_but = QPushButton(vol_widget)
        self.min_vol_but.setIcon(QIcon("Assets/sound.png"))
        self.min_vol_but.setIconSize(QSize(20,20))
        self.min_vol_but.setSizePolicy(but_size_policy)
        self.min_vol_but.setStyleSheet("background-color : transparent")
        self.min_vol_but.resize(QSize(20,20))
        self.min_vol_but.setToolTip("Mute")
        
        # Volume Slider
        self.vol_slider = QSlider(Qt.Horizontal,vol_widget)
        self.vol_slider.setRange(0,100)
        self.vol_slider.setMaximumWidth(150)
        self.vol_slider.setMinimumWidth(50)
        
        # Creating a layout to store them
        vol_h_layout = QHBoxLayout(vol_widget)
        vol_h_layout.addWidget(self.min_vol_but)
        vol_h_layout.addWidget(self.vol_slider)
        
        vol_widget.setLayout(vol_h_layout)
        vol_widget.show()
        
        # Image Layout
        image_layout.addStretch()
        image_layout.addWidget(self.image_label)
        image_layout.addStretch()
        
        self.image_widget.setLayout(image_layout)
        self.image_widget.show()
        
       
        # Adding the items to the info layout
        info_layout.addWidget(self.current_time)
        info_layout.addWidget(self.time_slider)
        info_layout.addWidget(self.end_time)
       
        # Adding the buttons to the layout
        playback_layout.addWidget(song_info)
        playback_layout.addStretch(5)
        playback_layout.addWidget(self.shuffle_but)
        playback_layout.addWidget(self.prev_but)
        playback_layout.addWidget(self.play_but)
        playback_layout.addWidget(self.next_but)
        playback_layout.addWidget(self.repeat_but)
        playback_layout.addStretch(5)
        playback_layout.addWidget(vol_widget)
        playback_layout.addWidget(self.queue_but)
        playback_layout.addStretch()
        
        # Adding this layout to the grid layout
        grid.rowStretch(20)
        grid.columnStretch(5)
        grid.addWidget(self.image_widget,0,0,15,5)
        grid.addLayout(info_layout,15,0,1,5)
        grid.addLayout(vol_layout,16,0,1,5)
        grid.addLayout(playback_layout,17,0,2,5)
        
        self.setLayout(grid)
    
    # Animating the text
    def animateText(self):
        current_text = self.song_name.text()
        new_text = current_text[1:] + current_text[0]
        self.song_name.setText(new_text)    
    
app = QApplication(sys.argv)
window = Test()
sys.exit(app.exec_())