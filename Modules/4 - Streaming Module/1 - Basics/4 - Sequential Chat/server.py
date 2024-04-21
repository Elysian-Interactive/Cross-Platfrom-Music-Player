# Importing the necessary modules
import socket
import sys

# Encompassing the whole process into a class

class ChatServer:
    # Constructor
    def __init__(self,host,port):
        # Declaring important variables
        self.server = None
        self.host = host
        self.port = port
        self.client = None
        self.client_addr = None
        self.ID = "Physical Machine"
        
        self.initialize()
    
    # Function to initialize and bind the host and port
    def initialize(self):
        # Creating a new socket object
        try:
            self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            # binding the host and the port
            self.server.bind((self.host,self.port))
            # listening and queueing the connections
            self.server.listen(5)
        except socket.error as msg:
            print("Server Creation Failed : " + str(msg))
            print("Terminating Process...")
            sys.exit()
    
    # Function to accept the incoming connect
    def acceptConnection(self):
        # Accepting the connections
        try:
            self.client,self.client_addr = self.server.accept()
            print("Connection made with : " + str(self.client_addr[0]))
        except socket.error as msg:
            print("Request Error :" + str(msg))
    
    # Function to receive any incoming data
    def receiveText(self):
        data = self.client.recv(1024).decode()
        # Checking if any data is sent
        if not data:
            # calling the send text method
            self.sendText()
        else:
            print(data)
        
        # again calling the send text method
        self.sendText()
    
    # Function to send the text
    def sendText(self):
        data = input(self.ID + " : ")
        data = self.ID + " : " + data
        self.client.send(str(data).encode())
        # calling the receive text method
        self.receiveText()
            
    # Function to close all the connections
    def closeServer(self):
        self.client.close()
        self.server.close()

    
            
            
    