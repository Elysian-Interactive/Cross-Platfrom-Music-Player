import sys
import Player as Pl
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout)

class TestPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.player = Pl.Player()
        self.player.load("music.mp3")
        self.initializeUI()
    
    def initializeUI(self):
        self.setWindowTitle("Player Test")
        self.setGeometry(100,100,400,400)
        self.setupUI()
        
        self.show()
    
    def setupUI(self):
    
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
        
        v_box = QVBoxLayout(self)
        v_box.addWidget(play_but)
        v_box.addWidget(pause_but)
        v_box.addWidget(resume_but)
        v_box.addWidget(rewind_but)
        v_box.addWidget(stop_but)
        v_box.addWidget(show_time)
        
        self.setLayout(v_box)
    
    # Function to 
    def displayTime(self):
        print(self.player.getElapsedTime())
        
        
def main():
    app = QApplication(sys.argv)
    window = TestPlayer()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
