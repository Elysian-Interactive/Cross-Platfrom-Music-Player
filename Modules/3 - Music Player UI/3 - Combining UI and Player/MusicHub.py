# Adding files to the path
import sys
sys.path.insert(0,"Dependencies")

from MusicPlayer import MusicPlayer
from MusicPlayerUI import MusicPlayerUI,VisibleSong
from List import List
from PyQt5.QtWidgets import QApplication,QFileDialog,QMessageBox,QFrame
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QSize, QTimer

# In this file we will connect the Player and UI part together

# Ok so we would need to create another class called visible playlist which would maintain
# the same instances of the music playlist

class MusicHub(MusicPlayerUI): # Inheriting the UI element
    # Constructor
    def __init__(self): 
        super().__init__() # Calling the parent of the constructor to initalize it
        # Creating certain required variables
        self.music_player = MusicPlayer() # Handles the playing of the music
        # Another variable will be the list of Visible Songs object to be displayed
        # in the scroll area
        self.visible_songs_list = List()
        # Function to setup certain functionalities for the buttons and other elements
        self.setupFunctions()
        
        self.show()
        
    # Function to initialize various functionalities
    def setupFunctions(self):
        
        # Setting the value of the volume slider to be 100 at start
        self.vol_slider.setValue(100)
    
        # Connecting the specific buttons to their respective signals
        self.add_song_but.clicked.connect(self.addSong)
        self.play_but.clicked.connect(self.pauseResumeSong)
        
       
    
        
    
    def addSong(self):
        # Opening the file dialog box to let the user select the songs
        filenames,_ = QFileDialog.getOpenFileNames(self,"Load Songs","","mp3 files (*.mp3);;wav files (*.wav);;ogg files(*.ogg);; All files (*.mp3 *.wav *.flac *.ogg)")
        # Adding those songs into the MusicPlayer's MusicPlayList
        self.music_player.addSongs(filenames)
        # Now again I also want to add the selected songs in the scroll area
        # But first they must be appended in the visible song list
        for i in self.music_player.playing_queue.songs_copy.getKeys():
            if i not in self.visible_songs_list.getKeys(): # This condition also takes care of redundant values
                # First we will create the widget and connect them with their specific signal
                widget = VisibleSong(i)
                # Connectint that widget to a method
                widget.play_song_but.clicked.connect(lambda _,w=widget:self.playSongFromScroll(w.title))
                self.songs_box.addWidget(widget)
                separator = QFrame(self)
                separator.setFrameShape(QFrame.HLine)  # Horizontal line separator
                separator.setFrameShadow(QFrame.Sunken)
                self.songs_box.addWidget(separator)
                # Now adding it to the list
                self.visible_songs_list.append(i,widget)
        
    def playSong(self):
        # While playing the song we must handle updating somethings
        # 1. Initializing the seekbar and set the end duration
        # 2. Calling the music player to play the songs
        # 3. Updating the seekbar periodically
        
        # 1. Retrieving the length of the song
        # It returns the song length in seconds
        song_length = int(self.music_player.playing_queue.current.getDuration())
        self.time_slider.setValue(0)
        self.time_slider.setRange(0,song_length)
        self.end_time.setText(" " + self.seconds_to_mm_ss(song_length))
        # 2. Playing the song
        self.music_player.playSong()
        
        # Also whenever this function is called we must change the icon on the play/pause button
        self.play_but.setIcon(QIcon("Assets/pause.png"))
        self.play_but.setIconSize(QSize(64,64))
        self.play_but.setStyleSheet("background-color : transparent")
        self.play_but.resize(QSize(64,64))
        
        # 3. Repeatedly updating the seek bar
        timer = QTimer(self)
        timer.timeout.connect(self.updateSeekBar)
        timer.start(1000)
        

    def playSongFromScroll(self,title):
        # Whenever we would play the song from the scroll area
        # There are certain things that must be done
        # 0. But first you must change the attributes of the already current element
        # 1. Identify which song element has called that signal
        # 2. Get the corresponding key and set that song to be the current 
        # 3. Update the texts and images accordingly
        # 4. Play the song
        # Better to divide these functionalities into different functions
        
        # 1. Updating the scroll area and setting current song
        self.updateScrollArea(title)
        # 2. Update the texts and iamges on the first page
        self.updateImageArea()
        # 4. Playing the song
        self.playSong()
    
    # Function to update the element in the scroll area
    def updateScrollArea(self,title):
        # Get the current song key and then update its color
        current_song_key = self.music_player.playing_queue.current.getTitle()
        # Now we have to set this current label color to be black instead of red
        current_widget_label = self.visible_songs_list.search(current_song_key).value.visible_title
        current_widget_button = self.visible_songs_list.search(current_song_key).value.play_song_but
        current_widget_label.setStyleSheet("color : black;")
        current_widget_button.setIcon(QIcon("Assets/small-play.png"))
        current_widget_button.setIconSize(QSize(20,20))
        current_widget_button.setStyleSheet("background-color : transparent")
        current_widget_button.resize(QSize(20,20))
        
        # Now find the new song to be played
        new_song_key = self.music_player.playing_queue.songs_copy.search(title).key
        new_widget_label = self.visible_songs_list.search(new_song_key).value.visible_title
        new_widget_button = self.visible_songs_list.search(new_song_key).value.play_song_but
        new_widget_label.setStyleSheet("color : red;")
        new_widget_button.setIcon(QIcon("Assets/playing.png"))
        new_widget_button.setIconSize(QSize(20,20))
        new_widget_button.setStyleSheet("background-color : transparent")
        new_widget_button.resize(QSize(20,20))
        
        # Now you would also need to update to be current song
        current_song = self.music_player.playing_queue.songs.search(title).value
        self.music_player.playing_queue.current = current_song
    
    # Function to update the elements in the image page plus the song info
    def updateImageArea(self):
        # Get the song title, artist and image location from the current song
        title = self.music_player.playing_queue.current.getTitle()
        artist = self.music_player.playing_queue.current.getArtist()
        image = self.music_player.playing_queue.current.getCover()
        
        self.song_name.setText(title + "    ")
        
        # Now we will check the conditions if any of the data is null
        if artist is None:
            self.artist_name.setText("Unknown")
        else:
            self.artist_name.setText(artist)
        
        # Now we will check if the image exists or not
        if image is None:
            pixmap = QPixmap("Assets/musical.png")
            pixmap = pixmap.scaled(500,500)
            self.image_label.setPixmap(pixmap)
        else:
            pixmap = QPixmap(image)
            pixmap = pixmap.scaled(500,500)
            self.image_label.setPixmap(pixmap)
            
        
    # Function to update the seek bar
    def updateSeekBar(self):
        current_value = self.music_player.player.getElapsedTime() # time in milli seconds
        current_value = int(current_value / 1000)
        self.time_slider.setValue(current_value)
        # Along with the seekbar we can also update our current time label
        self.current_time.setText(self.seconds_to_mm_ss(current_value))
    
    # Function to convert the seconds to the format mm:ss
    def seconds_to_mm_ss(self,seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    
    def pauseResumeSong(self):        
        self.music_player.pauseResumeSong()
        # Here we want to make sure
        
        if self.music_player.player.isPlaying():
            if not self.music_player.player.PAUSED:
                self.play_but.setIcon(QIcon("Assets/pause.png"))
                self.play_but.setIconSize(QSize(64,64))
                self.play_but.setStyleSheet("background-color : transparent")
                self.play_but.resize(QSize(64,64))
  
        elif not self.music_player.player.isPlaying():
            if self.music_player.player.PAUSED:
                self.play_but.setIcon(QIcon("Assets/play-button.png"))
                self.play_but.setIconSize(QSize(60,60))
                self.play_but.setStyleSheet("background-color : transparent")
                self.play_but.resize(QSize(60,60))  

    
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
    window = MusicHub()
    sys.exit(app.exec_())

# Calling the main Function
main()
    
