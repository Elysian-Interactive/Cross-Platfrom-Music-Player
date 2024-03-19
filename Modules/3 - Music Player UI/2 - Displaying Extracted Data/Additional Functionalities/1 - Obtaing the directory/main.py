# In this script we will open a directory
# and then try to print its contents on the screen

import sys
from pathlib import Path
from Player import Player
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QFileDialog

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.initializeUI()
    
    def initializeUI(self):
        self.setWindowTitle("Opening Folders")
        self.setGeometry(100,100,400,400)
        self.setupTest()
        
        self.show()
    
    def setupTest(self):
        open_but = QPushButton("Open Folders",self)
        open_but.clicked.connect(self.openFolders)
        
    def openFolders(self):
        folder = QFileDialog.getExistingDirectory(self,"Select Directory")
        if folder:
            # This is one way to do it 
            '''
            files = glob(folder + "/*.*")
            print(files)
            '''
            # Another way
            directory = Path(folder)
            files = []
            for item in directory.glob("*.mp3"):
                files.append(item)
            
            # Playing the music files after reading them
            self.player.load(files[0])
            self.player.play()
                
        else:
            print("No Directory Selected")
    
app = QApplication(sys.argv)
window = Test()
sys.exit(app.exec_())