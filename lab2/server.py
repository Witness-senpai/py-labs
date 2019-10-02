import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 1234))
#sock.listen(2)

clients = []

while True:
    clients.append(sock.accept())
    msg = sock.recv(1024)
    print(msg.decode('utf-8'))  
    #clients[0][0].send(bytes("sas", "utf-8"))
    
    #Когда оба клиента подключены
    if len(clients) == 2:
        msg = sock.recv(1024)
        print(msg.decode('utf-8'))

    
clients[0].close()