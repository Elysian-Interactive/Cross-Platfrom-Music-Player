# This module will combine all of the other modules to use them
# It will implment its own loading, playback, playlist handler functions

# Test 2 : This test will check for pause,resume,next,previous plus rewind to be included in previous functionality

from Player import Player
from Song import Song
from PlayList import PlayList
from Extractor import Extractor
from List import List
import pickle # Used for serializing and here for saving playlists to disc

# Creating a custom playlist class to handle certain other features such as shuffle,repeat etc
class MusicPlayList(PlayList):
    # Constructor
    def __init__(self,name):
        # Calling the super class's constructor
        super().__init__(name)
        # Defining two new attribute
        self.SHUFFLE = False
        self.REPEAT = False
        # and defining a new list which will be responsible for operations like shuffle, sorting etc
        self.songs_copy = List()
        # The add and remove functions must be overwritten for this class
    
    def add(self,song):
        if self.current is None:
            self.current = song
        # Adding the song into the list
        # as (key : Title, Value : Song Object)
        self.songs.append(song.getTitle(),song)
        # Also we will define which playlist the song belongs to
        self.songs.search(song.getTitle()).value.setPlayList(self.name)
        

class MusicPlayer:
    # Constructor
    def __init__(self):
        # Maintains its own playing queue
        # When you wish to load or create a playlist you can do so with its help
        self.playing_queue = MusicPlayList("Current Queue")
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
    
    # Function to pause the song
    def pauseResumeSong(self):
        # We will go through a couple of conditions first
        # before pausing the playback
        
        # First we will check if anything is being played or not
        if self.player.isPlaying():
            # Now again checking the state of the player if it is paused
            if not self.player.PAUSED:
                # Now we can pause the song
                self.player.pause()
        # Again we will check if the player is playing or not
        # and if it is not then we will resume the song else nothing happens
        elif not self.player.isPlaying():
            if self.player.PAUSED:
                # Now we can resume the song
                self.player.resume()
        


    
    
        
    
        
            