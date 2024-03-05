import sys
import Player as Pl
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout,QFileDialog)

class TestPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.player = Pl.Player()
        self.initializeUI()
    
    def initializeUI(self):
        self.setWindowTitle("Player Test")
        self.setGeometry(100,100,400,400)
        self.setupUI()
        
        self.show()
    
    def setupUI(self):
    
        load_but = QPushButton("Load",self)
        load_but.clicked.connect(self.loadMusic)
    
        play_but = QPushButton("Play",self)
        play_but.clicked.connect(self.player.play)
        
        pause_but = QPushButton("Pause",self)
        pause_but.clicked.connect(self.player.pause)
        
        resume_but = QPushButton("Resume",self)
        resume_but.clicked.connect(self.player.resume)
        
        rewind_but = QPushButton("Rewind",self)
        rewind_but.clicked.connect(self.player.rewind)
        
        stop_but = QPushButton("Stop",self)
        stop_but.clicked.connect(self.player.stop)
        
        show_time = QPushButton("Get Time",self)
        show_time.clicked.connect(self.displayTime)
        
        dec_vol = QPushButton("Decrease Volume",self)
        dec_vol.clicked.connect(self.decreaseVolume)
        
        inc_vol = QPushButton("Increase Volume",self)
        inc_vol.clicked.connect(self.increaseVolume)
        
        show_vol = QPushButton("Current Volume")
        show_vol.clicked.connect(self.showVolume)
        
        show_songs = QPushButton("Playing")
        show_songs.clicked.connect(self.displaySongs)
        
        v_box = QVBoxLayout(self)
        v_box.addWidget(load_but)
        v_box.addWidget(play_but)
        v_box.addWidget(pause_but)
        v_box.addWidget(resume_but)
        v_box.addWidget(rewind_but)
        v_box.addWidget(stop_but)
        v_box.addWidget(show_time)
        v_box.addWidget(dec_vol)
        v_box.addWidget(inc_vol)
        v_box.addWidget(show_vol)
        v_box.addWidget(show_songs)
        
        self.setLayout(v_box)
    
    def displaySongs(self):
        print(self.player.playing_queue.getQueueInfo())
    
    # Function to 
    def displayTime(self):
        print(self.player.getElapsedTime())
        
    # Function to dynamically load the music 
    def loadMusic(self):
        file_name, _ = QFileDialog.getOpenFileName(self,"Open Music Files","","MP3 Files (*.mp3);; WAV Files(*.wav);; OGG Files(*.ogg)")
        
        if file_name:
            if self.player.isPlaying():
                self.player.stop()
                self.player.unload()
                
                self.player.load(file_name)
                self.player.play()
            else:
                self.player.unload()
                self.player.load(file_name)
                self.player.play()
        else:
            print("Unable to open file")
        
    # Functions to handle the volume
    def showVolume(self):
        cur_vol = self.player.getVolume() * 100
        print(cur_vol)
    
    def decreaseVolume(self):
        new_vol = self.player.getVolume() - 0.1
        self.player.setVolume(new_vol)
    
    def increaseVolume(self):
        new_vol = self.player.getVolume() + 0.1
        self.player.setVolume(new_vol)
    
def main():
    app = QApplication(sys.argv)
    window = TestPlayer()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
