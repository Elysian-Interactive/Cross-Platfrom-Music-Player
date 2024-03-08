# Test file for playlists

import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout,QFileDialog)
import Extractor
import Song
import PlayList

class Test(QWidget):
    def __init__(self):
        super().__init__()
        # Variables
        self.extractor = Extractor.Extractor()
        self.playlist = PlayList.PlayList("Queue")
        self.song = None
        # functions
        self.initializeUI()
        
    
    def initializeUI(self):
        self.setWindowTitle("Testing Playlist")
        self.setGeometry(100,100,400,400)
        self.setupTest()
        
        self.show()
    
    def setupTest(self):
        # Buttons
        load_but = QPushButton("Load Song",self)
        load_but.clicked.connect(self.loadSong)
        
        extract_but = QPushButton("Extract Data",self)
        extract_but.clicked.connect(self.extractData)
        
        add_to_pl_but = QPushButton("Add to Playlist",self)
        add_to_pl_but.clicked.connect(self.addToPlaylist)
        
        show_pl_but = QPushButton("Show Playlist",self)
        show_pl_but.clicked.connect(self.showPlaylist)
        
        v_box = QVBoxLayout(self)
        v_box.addWidget(load_but)
        v_box.addWidget(extract_but)
        v_box.addWidget(add_to_pl_but)
        v_box.addWidget(show_pl_but)

        self.setLayout(v_box)
        
    def loadSong(self):
        filename,_ = QFileDialog.getOpenFileName(self,"Load Songs","","mp3 files (*.mp3);; wav files(*.wav);; ogg files (*.ogg);; flac files (*.flac);; All Files (*.*)")
        
        if filename:
            self.song = Song.Song()
            self.song.setFile(filename)
    
    def extractData(self):
        self.extractor.loadSong(self.song)
        self.song = self.extractor.getSong()
        
    def addToPlaylist(self):
        self.playlist.add(self.song)
        
    def showPlaylist(self):
        self.playlist.songs.display()
    
def main():
    app = QApplication(sys.argv)
    window = Test()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
        

