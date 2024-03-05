# This module will represent a song as an entity and would comprise of 
# the details associated with the song like name, artist, album, cover art etc

class Song:
    # Constructor
    def __init__(self):
        # Song attributes
        self.title = None # Title of the Song
        self.artist = None # Artists' name
        self.album = None # Album's name
        self.duration = None # Length of the song
        self.location = None # File location of the song
        self.cover = None # Album cover art of the song
        self.playing = None # Boolean value defines if the song is currently 
                            # playing or not
        self.format = None # Defines the format of the song
    
    # Utility functions
    
    # SETTER FUNCTIONS
    def setTitle(title):
        self.title = title
    
    def setArtist(artist):
        self.artist = artist
    
    def setAlbum(album):
        self.album = album
    
    def setDuration(duration):
        self.duration = duration
    
    def setPlaying(state):
        self.playing = state
    
    def setFormat(format):
        self.format = format
    
    # GETTER FUNCTIONS
    def getTitle():
        return self.title
    
    def getArtist():
        return self.artist
    
    def getAlbum():
        return self.album
    
    def getDuration():
        return self.duration
    
    def getPlaying():
        return self.playing
    
    def getFormat():
        return self.format
    
    
        