import sys
import Song
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout,QFileDialog)

class TestPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.song = Song.Song()
        self.initializeUI()
    
    def initializeUI(self):
        self.setWindowTitle("Extractor Test")
        self.setGeometry(100,100,400,400)
        self.setupUI()
        
        self.show()
    
    def setupUI(self):
    
        load_but = QPushButton("Load",self)
        load_but.clicked.connect(self.loadMusic)
        
        show_format = QPushButton("Show Format",self)
        show_format.clicked.connect(self.showFormat)
        
        file_loc = QPushButton("Show File Location",self)
        file_loc.clicked.connect(self.showFileLoc)
    
        v_box = QVBoxLayout(self)
        v_box.addWidget(load_but)
        v_box.addWidget(show_format)
        v_box.addWidget(file_loc)
        self.setLayout(v_box)
   
    # Function to dynamically load the music 
    def loadMusic(self):
        file_name, _ = QFileDialog.getOpenFileName(self,"Open Music Files","","MP3 Files (*.mp3);; WAV Files(*.wav);; OGG Files(*.ogg)")
        
        if file_name:
            self.song.setFile(file_name)
        else:
            print("Unable to open file")
        
    def showFormat(self):
        if self.song.getFormat() != None:
            print(self.song.getFormat())
        else:
            print("No format")
        
    def showFileLoc(self):
        if self.song.getFile() != None:
            print(self.song.getFile())
        else:
            print("No file")
    
def main():
    app = QApplication(sys.argv)
    window = TestPlayer()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
