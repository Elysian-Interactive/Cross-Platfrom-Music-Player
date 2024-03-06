# This module will be responsible for extracting the metadata from the 
# song like title of the song, artist's name, album name, cover art etc

# importing required modules
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
from mutagen.wave import WAVE

class Extractor:
    
    # Constructor
    def __init__(self,song):
        # We will pass the song object to it so that it can get all the data
        # and possibly update all of that data too
        self.song = song
        # Variable to store the metadata
        self.metadata = {}
        
    # Function to retrieve all of the data
    def setData(self):
        # Retrieving the data from the song file
        if self.song.getFormat() == "mp3":
            audio = MP3(self.song.getFile())
            self.metadata = audio.tags
            
        elif self.song.getFormat() == "wav":
            audio = WAVE(self.song.getFile())
            self.metadata = audio
            
        elif self.song.getFormat() == "ogg":
            audio = OggVorbis(self.song.getFile())
            self.metadata = audio
            
        elif self.song.getFormat() == "flac":
            audio = FLAC(self.song.getFile())
            self.metadata = audio
        
    # Function to display that data
    def showData(self):
        print(self.metadata)
    

    
    
            

        