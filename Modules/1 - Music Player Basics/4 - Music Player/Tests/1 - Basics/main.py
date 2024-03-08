# test file
import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QFileDialog,QVBoxLayout)
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
        
        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(load_but)
        v_box.addWidget(play_but)
        v_box.addStretch()
        
        self.setLayout(v_box)
        
    
    def loadSong(self):
        filenames,_ = QFileDialog.getOpenFileNames(self,"Load Songs","","mp3 files (*.mp3);;wav files (*.wav);;ogg files(*.ogg);; All files (*.*)")
        self.m_player.addSongs(filenames)
    
    def playSong(self):
        self.m_player.playSong()
        
def main():
    app = QApplication(sys.argv)
    window = Test()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
