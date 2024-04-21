# Now this will be a bit lengthy as we will be doing some more work
import socket
import tqdm # This provides great progress bars

# Now we will setup the server side and listen for the connection
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# binding the server to the host and port
server.bind(("",9999))
# Now listening for active connection
server.listen()

# After listening to the connections we will accept the connection
# Now recall that the client send two things : 1. connection object 2. address

client,addr = server.accept()

# Now we will read the data sent by the client
file_name = client.recv(1024).decode()
print(file_name)
file_size = client.recv(1024).decode()
print(file_size)

# Now we will read and save the file
file = open(file_name,'wb')

# Now we will create a byte string onto which we will append the incoming data
file_bytes = b''

# Setting up the progress bar
progress = tqdm.tqdm(unit = "8",unit_scale = True,unit_divisor = 1000,
                     total = int(file_size))

done = False # variable to let us know when to stop reading

# continously reading and appending the data
while not done:
    data = client.recv(1024)
    if file_bytes[-5:] == b'<END>': # we check for the tag in the string not in the stream
        done = True                 # bcz the stream is not always continous and the comparison
    else:                           # would not always result successful
        file_bytes += data # Appending data to the string
    progress.update(1024)
    
# Now finally writing the data on the disk
file.write(file_bytes)

# Closing all the streams
file.close()
client.close()
server.close()
    