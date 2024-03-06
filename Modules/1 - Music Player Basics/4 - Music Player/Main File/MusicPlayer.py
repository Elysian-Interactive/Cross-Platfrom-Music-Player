# This module will combine all of the other modules to use them
# It will implment its own loading, playback, playlist handler functions

from Player import Player
from Song import Song
from PlayList import PlayList
from Extractor import Extractor

class MusicPlayer:
    # Constructor
    def __init__(self):
        # Maintains its own playing queue
        # When you wish to load or create a playlist you can do so with its help
        self.playing_queue = PlayList("Current Queue")
        # This is the part of the music player which actually plays the music
        self.player = Player()
        # This is the metadata extractor module 
        self.extractor = Extractor()
        # A song object which acts as a intermediary for loading and playing things
        self.song = Song()
        
    # Loading a single song
    def loadSong(self,filename):
        pass
    
    # Loading multiple songs
    def loadSongs(self,filenames):
        pass
    
    
        
    
        
            