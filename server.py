import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 3000))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    s=input('Message to be sent to client: ')
    conn.send(s.encode('utf8'))
    x = conn.recv(1024).decode()
    print('Message received from client: ' + x) 
    serv.close()
    break