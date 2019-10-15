import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 3125))
sock.listen(2)

clients = []

print("===ЛОГ АГЕНТА===")
print("Ожидания клиентов для перехвата данных...")

while True:
    clients.append(sock.accept())

    #Когда оба клиента подключены
    if len(clients) == 2:
        #После подключения клиентов, сообщаем им что их собеседники готов
        clients[0][0].send('go'.encode())
        clients[1][0].send('go'.encode())

        #Получаем их имена просто для наглядности алгоритма
        name1 = clients[0][0].recv(1024).decode('utf-8')
        name2 = clients[1][0].recv(1024).decode('utf-8')
        print(f"Прослушиване клиентов: {name1} и {name2}")

        input() #Для вывода имформации на консоль только после нажатия на enter

        #Получение данных от первого клиента
        msg = clients[0][0].recv(1024).decode("utf-8") 
        msg = msg.split('\n')
        g = msg[0]
        p = msg[1]
        A = msg[2]
        print(f"Перехват данных: {name1} -> {name2}:\ng = {g}\np = {p}\nA = {A}")

        input()

        #Переправка полученных данных второму клиенту
        clients[1][0].send((str(g) + "\n" + str(p) + "\n" + str(A)).encode())

        input()

        #Получение данных(число B) от второго клиента
        B = clients[1][0].recv(1024).decode("utf-8")
        print(f"Перехват данных: {name2} -> {name1}:\nB = {B}")

        input()

        #Переправка данных первому клиенту
        clients[0][0].send(B.encode())

        print(f"Секретный ключ K = {A}^b mod {p} = {B}^a mod {p}")
        
        clients[0][0].close()
        clients[1][0].close()
        break