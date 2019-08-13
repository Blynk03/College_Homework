import sys
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethosetbyname(socket.gethostname())
PORT = 1456
address=(IP,PORT)
server.bind(address)
server.listen(1)
print("Start listening on port " + PORT)
client,
