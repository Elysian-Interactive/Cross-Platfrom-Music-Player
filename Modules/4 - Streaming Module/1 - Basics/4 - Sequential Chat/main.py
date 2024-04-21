# Script to run the chat application
from server import ChatServer
import threading

# Initialization part
chat_server = ChatServer("",9999)
chat_server.acceptConnection()

# Creating threads for sending and receiving data
send_thread = threading.Thread(target = chat_server.sendText())
recv_thread = threading.Thread(target = chat_server.receiveText())

# Starting the threads
recv_thread.start()
