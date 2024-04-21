import socket

server = socket.socket()

server.bind(('',9999))

server.listen()

client,addr = server.accept()

data = client.recv(1024).decode()

print(data)