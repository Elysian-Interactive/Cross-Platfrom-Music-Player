# Adding files to the path
import sys
sys.path.insert(0,"Dependencies")

# This file will mainly focus on adding buttons to the UI for:
# 1. Pause/Play , forward, rewind, volume, shuffle, rewind
# 2. The Slider which depicts time elapsed of the song
# 3. Displaying the extracted metadata on the screen 

# Importing the necessary modules
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QFileDialog,QVBoxLayout
                            ,QHBoxLayout,QGridLayout,QSlider,QMenuBar,QStatusBar,QAction
                            ,QMenu)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from MusicPlayer import MusicPlayer

class MusicPlayerUI(QWidget):
    # Constructor
    def __init__(self): 
        super().__init__()
        self.music_player = MusicPlayer()
        self.initializeUI()
        
    def initializeUI(self):
        self.setWindowTitle("MusicHub")
        self.setGeometry(100,100,400,400)
        self.setupMenus()
        self.setupButtons()

        
        self.show()
    
    def setupButtons(self):
        load_but = QPushButton("Load Song",self)
        load_but.clicked.connect(self.loadSong)
        
        play_but = QPushButton("Play Song",self)
        play_but.clicked.connect(self.playSong)
        
        pause_resume_but = QPushButton("Pause/Resume",self)
        pause_resume_but.clicked.connect(self.pauseResumeSong)
        
        next_but = QPushButton("Next",self)
        next_but.clicked.connect(self.nextSong)
        
        prev_but = QPushButton("Prev",self)
        prev_but.clicked.connect(self.prevSong)
        
        shuffle_but = QPushButton("Shuffle",self)
        shuffle_but.clicked.connect(self.shuffle)
        
        repeat_but = QPushButton("Repeat",self)
        repeat_but.clicked.connect(self.repeat)
       
        
        # Connecting the new signal to the handle event
        self.m_player.player.sound_finished.connect(self.handleEndEvent)
        
        h_box = QHBoxLayout()
        h_box.addWidget(shuffle_but)
        h_box.addWidget(prev_but)
        h_box.addWidget(pause_resume_but)
        h_box.addWidget(next_but)
        h_box.addWidget(repeat_but)
        
        v_box = QVBoxLayout()
        v_box.addWidget(load_but)
        v_box.addWidget(play_but)
        v_box.addLayout(h_box)

        
        self.setLayout(v_box)
        
    
    def loadSong(self):
        filenames,_ = QFileDialog.getOpenFileNames(self,"Load Songs","","mp3 files (*.mp3);;wav files (*.wav);;ogg files(*.ogg);; All files (*.*)")
        self.m_player.addSongs(filenames)
    
    def playSong(self):
        self.m_player.playSong()
    
    def pauseResumeSong(self):
        self.m_player.pauseResumeSong()
    
    def nextSong(self):
        self.m_player.playNextSong()
    
    def prevSong(self):
        self.m_player.playPreviousSong()
    
    def handleEndEvent(self):
        self.m_player.handleEndEvent()
        
    def repeat(self):
        self.m_player.toggleRepeat()
    
    def shuffle(self):
        self.m_player.toggleShuffle()
    
    def getLength(self):
        print(len(self.m_player.playing_queue.songs))

        
def main():
    app = QApplication(sys.argv)
    window = MusicPlayerUI()
    sys.exit(app.exec_())

# Calling the main Function
main()
    
