# The aim of this program is to implement features such as

# -> Play
# -> Pause
# -> Rewind
# -> Stop
# -> Volume

# The working of this module will be as followings:

# 1. We will have a global music object onto which the music files will be loaded or unloaded
# 2. Different methods indicating the function to be implemented such as play,pause,stop etc

import pygame
from pygame import mixer
# for handling events in pyqt you must define your own signals and slots 
# but for now we can simply check the length of the elapsed time againsts
# that of defined by the player

class Player:

    # Constructor
    def __init__(self):
        # Initializing the mixer
        mixer.init() # Enables the playback
        # Creating a music object which will store and play all the sound
        self.music = mixer.music
        # Different kinds of events must be declared before hand
        self.NEXT = pygame.USEREVENT + 1 # Custome Event
        
        print("MESSAGE : Player Initialization Successful")
        
    # Function to load the music file
    def load(self,filename):            
        # Loads the music in to the music object
        self.music.load(filename)
        # Adding the file to the playing queue

    
    # Function to check if the music is already playing
    def isPlaying(self):
        if self.music.get_busy():
            return True
        else:
            return False
    
    # Function to start playing the sound
    def play(self):
        try:
            self.music.play()
        except pygame.error:
            print("No music file is loaded")
    
    # Function to pause the music
    def pause(self):
        self.music.pause()
    
    # Function to rewind the music
    def rewind(self):
        self.music.rewind()
    
    # Function to resume music once its paused
    def resume(self):
        self.music.unpause()
    
    # Function to stop the play back 
    def stop(self):
        self.music.stop()
    
    # Function to unload the resources
    def unload(self):
        self.music.unload()
    
    # Function to get the volume of the music
    def getVolume(self):
        return self.music.get_volume() # Returns a float value between 0.0 and 1.0
        
    # Function to set the volume of the music
    def setVolume(self,volume):
        self.music.set_volume(volume) # Accepts a value between 0.0 and 1.0
        # If value greater than 1.0 is given it will automatically set it to 1.0
        
    # Function to queue up next sound such that it may play exactly after
    # the current sound finishes
    def queueUpNext(self,filename):         
        # Loads the music in to the music object
        self.music.queue(filename)
        
    
    # Function to get the elapsed time
    def getElapsedTime(self):
        try:
            return self.music.get_pos() # Returns the time in milliseconds
        except pygame.error:
            print("No music file is loaded")
            
    
    # Function to set the elapsed time
    def setElapsedTime(self,pos):
        self.muisc.set_pos(pos)

# EndEvent handling is left

    def setEndEvent(self,event):
        # Sends an event to the mixer
        self.music.set_endevent(event)
        
    
        