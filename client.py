import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 3000))
while True:
    print('Message received from server: ' + client.recv(1024).decode())
    s=input('Message to be sent to server: ')
    client.send(s.encode('utf8'))
    client.close()
    break
