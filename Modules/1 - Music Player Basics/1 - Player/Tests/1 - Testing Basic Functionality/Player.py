# The aim of this program is to implement features such as

# -> Play
# -> Pause
# -> Rewind
# -> Stop
# -> Volume

# The working of this module will be as followings:

# 1. We will have a global music object onto which the music files will be loaded or unloaded
# 2. Different methods indicating the function to be implemented such as play,pause,stop etc

from pygame import mixer

class Player:

    # Constructor
    def __init__(self):
        # Initializing the mixer
        mixer.init() # Enables the playback
        # Creating a
        self.music = mixer.music
        print("MESSAGE : Player Initialization Successful")
        
    # Function to load the music file
    def load(self,filename):
        
        # Categorizing the file format of the file
        if filename.endswith('.mp3'):
            self.format = 'mp3'
        elif filename.endswith('.wav'):
            self.format = 'wav'
        elif filename.endswith('.ogg'):
            self.format = 'ogg'
        elif filename.endswith('.aac'):
            self.format = 'aac'
        else:
            self.format = 'other'
            
        # Loads the music in to the music object
        self.music.load(filename)
    
    # Function to check if the music is already playing
    def isAlreadyPlaying(self):
        if self.music.get_busy():
            return True
        else:
            return false
    
    # Function to start playing the sound
    def play(self):
        self.music.play()
    
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
        
    # Function to queue up next sound such that it may play exactly after
    # the current sound finishes
    def queueUpNext(self,filename):
    
        # Categorizing the file format of the file
        if filename.endswith('.mp3'):
            self.format = 'mp3'
        elif filename.endswith('.wav'):
            self.format = 'wav'
        elif filename.endswith('.ogg'):
            self.format = 'ogg'
        elif filename.endswith('.aac'):
            self.format = 'aac'
        else:
            self.format = 'other'
            
        # Loads the music in to the music object
        self.music.queue(filename)
    
    # Function to get the elapsed time
    def getElapsedTime(self):
        return self.music.get_pos() # Returns the time in milliseconds
    
    # Function to set the elapsed time
    def setElapsedTime(self,pos):
        self.muisc.set_pos(pos)
        
# TEST CASE SCENARIOS:
# What if there is no file loaded and we try to play it
# How to handle pygame.error in code
