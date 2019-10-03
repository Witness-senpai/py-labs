import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 3125))
sock.listen(2)

clients = []

while True:
    clients.append(sock.accept())

    #Когда оба клиента подключены
    if len(clients) == 2:
        #Получение данных от первого клиента
        msg = clients[0][0].recv(1024).decode("utf-8") 
        msg = msg.split('\n')
        a = msg[1]
        g = msg[2]
        p = msg[3]
        A = msg[4]
        print("a = " + str(a) + "\ng = " + str(g) + "\np = " + str(p) + "\nA = " + str(A))

        #Отправка полученных данных второму клиенту
        clients[1][0].send((str(a) + "\n" + str(g) + "\n" + str(p) + "\n" + str(A)).encode())

        #Получение данных(число B) от второго клиента
        B = clients[1][0].recv(1024).decode("utf-8")
        print("B = " + B)
        #Переправка первому клиенту
        clients[0][0].send(B.encode())
        

clients[0][0].close()