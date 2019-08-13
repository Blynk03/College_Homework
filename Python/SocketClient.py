import socket
client=socket.socket()
client.connect(('10.31.66.163', 1456))

def call(data):
    client.send(data.encode())
    print(client.recv(1024))
call("Hello Server")
