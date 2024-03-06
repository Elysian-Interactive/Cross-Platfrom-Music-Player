import sys
import Song
import Extractor
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout,QFileDialog)

class TestPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.song = Song.Song()
        self.extractor = None
        self.initializeUI()
    
    def initializeUI(self):
        self.setWindowTitle("Extractor Test")
        self.setGeometry(100,100,400,400)
        self.setupUI()
        
        self.show()
    
    def setupUI(self):
    
        load_but = QPushButton("Load",self)
        load_but.clicked.connect(self.loadMusic)
        
        extract_data = QPushButton("Extract Data",self)
        extract_data.clicked.connect(self.extractData)
        
        show_data = QPushButton("Show Data",self)
        show_data.clicked.connect(self.showData)
        
        print_data = QPushButton("Print Data",self)
        print_data.clicked.connect(self.printData)
    
        v_box = QVBoxLayout(self)
        v_box.addWidget(load_but)
        v_box.addWidget(extract_data)
        v_box.addWidget(show_data)
        v_box.addWidget(print_data)
        self.setLayout(v_box)
   
    # Function to dynamically load the music 
    def loadMusic(self):
        file_name, _ = QFileDialog.getOpenFileName(self,"Open Music Files","","MP3 Files (*.mp3);; \
        WAV Files(*.wav);; OGG Files(*.ogg) ;; FLAC Files (*.flac) ;; All Files (*.*)")
        
        if file_name:
            self.song.setFile(file_name)
        else:
            print("Unable to open file")
    
    def extractData(self):
        self.extractor = Extractor.Extractor(self.song)
        self.extractor.getData()
    
    def showData(self):
        self.extractor.setData()
    
    def printData(self):
        self.song = self.extractor.getSong()
        print(self.song)
        
    
def main():
    app = QApplication(sys.argv)
    window = TestPlayer()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
