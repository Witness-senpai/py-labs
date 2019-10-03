import socket
import random

#некое множество простых чисел
simples = [3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517]
#Числа a, b, g генерируются случайно, p - простое число берётся из simples

name = input("Введите ваше имя: ")
key = input("Хотите сгенерировать случайные параметры? (y/n)  ")

sock = socket.socket()
sock.connect((socket.gethostname(), 3125)) 

while True:
    if sock.recv(1024).decode('utf-8') == 'go':
        #Отправка своего имени вне зависимо от режима
        sock.send(name.encode())
        print("===ЛОГ КЛИЕНТА " + name.upper() + "===")
        if 'y' in key:
            a = random.randint(100, 500)
            g = random.randint(10, 20)
            p = simples[random.randint(0, len(simples) - 1)]
            print(f"Генерация данных: \na = {a}\ng = {g}\np = {p}\nA = {g ** a % p}")

            #Отправка сгенерированных данных второму клиенту
            print("Отправка собеседику: g, p, A")
            sock.sendall((str(g) + "\n" + str(p) + "\n" + str((g ** a) % p)).encode())
            print("Ожидание значения B от собеседника...")
            
            #Получение от второго клиента числа B, сгенерированного на основе отправленных данных
            B = int(sock.recv(1024).decode("utf-8"))
            print(f"От собеседника пришло B = {B}")

            #Генерация ключа
            K = B ** a % p
            print(f"Генерация общего секретного ключа: K = B^a mod p = {B}^{a} mod {p} = {K}")
        else:
            b = random.randint(100, 500)
            print(f"Генерирую значение b = {b}")
            print("Ожидаю значения g, p, A...")

            #Получение сгенерированных данных
            msg = sock.recv(1024).decode("utf-8").split('\n')
            g = msg[0]
            p = msg[1]
            A = msg[2]
            print(f"От собеседника пришло: \ng = {g}\np = {p}\nA = {A}")

            #Формирование на их основе ещё одного числа и его отправка
            B = (int(g) ** int(b)) % int(p)
            print(f"Генерирую B = g^b mod p = {B}")
            print("Отправляю сгенерированное значение В собеседнику")
            sock.sendall(str(B).encode())
            
            #Генерация ключа
            K = int(A) ** int(b) % int(p)
            print(f"Генерация общего секретного ключа: K = A^b mod p = {A}^{b} mod {p} = {K}")
