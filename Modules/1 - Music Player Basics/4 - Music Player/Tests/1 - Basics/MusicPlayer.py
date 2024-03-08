# This module will combine all of the other modules to use them
# It will implment its own loading, playback, playlist handler functions

from Player import Player
from Song import Song
from PlayList import PlayList
from Extractor import Extractor
import pickle # Used for serializing and here for saving playlists to disc

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
        
    # Loading a single song
    def addSong(self,filename):
        # Loading the song into a temporary object
        self.song = Song()
        self.song.setFile(filename)
        # Extracting the data from the song
        self.extractor.loadSong(self.song)
        self.song = self.extractor.getSong()
        # Adding this object to the playlist
        self.playing_queue.add(self.song)
    
    # Loading multiple songs
    def addSongs(self,filenames):
        # Loads multiple files at once
        for f in filenames:
            self.addSong(f)
    
    # Function to play the song
    def playSong(self):
        # First checking if there exists any song in the playing queue
        if self.playing_queue.isEmpty():
            pass
        else:
            # Unloading the current resource from the player
            self.player.unload()
            # Retreiving the file from the current song in the playlist
            song_file = self.playing_queue.current.getFile()
            # Passing this file to be loaded into the player
            self.player.load(song_file)
            # Now playing the song
            self.player.play()
    
    
        
    
        
            