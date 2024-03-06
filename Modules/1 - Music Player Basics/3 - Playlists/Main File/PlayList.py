# This module will be responsible for storing the music files and providing them to 
# the player when needed such that it can play those required sounds

from pathlib import Path

class PlayList:
    
    # Constructor
    def __init__(self,name):
        # Name of the playlist
        self.name = name
        # Photo Cover of the playlists
        self.cover = None
        # List of songs to be played 
        self.songs = {}
    
    # Function to add songs to the playlist
    # Check if the song already exists then display a prompt to the user
    def add(self,song):
        # Adding the song to the playlist
        self.songs[song_name] = filename
        
    # Function to remove the song from the playlist
    def remove(self,song_name):
        self.songs.pop(song_name)
    
    # Function to return the dictionary containing the information
    def getQueueInfo(self):
        return self.songs
       
        
        
        