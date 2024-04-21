import socket

client = socket.socket()

client.connect(("127.0.0.1",9999))

client.send("Hi from physical machine".encode())

client.close()