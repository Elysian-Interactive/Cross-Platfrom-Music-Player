# test file
import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QFileDialog,QVBoxLayout,QHBoxLayout)
from MusicPlayer import MusicPlayer

class Test(QWidget):
    def __init__(self): 
        super().__init__()
        self.m_player = MusicPlayer()
        self.initializeUI()
        
    def initializeUI(self):
        self.setWindowTitle("Music Player Test")
        self.setGeometry(100,100,400,400)
        self.setupTest()
        
        self.show()
    
    def setupTest(self):
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
        
        get_len_but = QPushButton("Get Length",self)
        get_len_but.clicked.connect(self.getLength)
        
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
        v_box.addWidget(get_len_but)

        
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
    window = Test()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
