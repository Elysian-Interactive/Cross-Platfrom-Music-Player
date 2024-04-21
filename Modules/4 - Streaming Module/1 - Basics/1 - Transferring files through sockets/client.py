# The client side will be easy as we will send the complete data 
# First we will make a connection
# Then we will send the file name
# Then the file size
# and finally the file itself

import os # We will be using this to obtain the size of the file
import socket

# First we will create the connection
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET means an internet socket of IPv4 address family 
                                                          # SOCK_STREAM determines a TCP connection
# Now connect with the server with the host and port
client.connect(("127.0.0.1",9999))

# Now open the file in read byte mode
file = open("Lucid Dreams.mp3",'rb')

# Now obtain the file size
file_size = os.path.getsize("Lucid Dreams.mp3")

# Now we will send this data to the server
# First we will send the file name
client.send("Music.mp3".encode()) # It is important to encode it in bytes
# Then we will send the file size 
client.send(str(file_size).encode())

# Now to send the file itself
data = file.read()
client.sendall(data)
# Now we will also send an end tag to let us know that the connection can be terminated now
client.send(b'<END>')


# Finally closing all the stream
file.close()
client.close()

