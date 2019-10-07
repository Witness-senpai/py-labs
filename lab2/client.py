import socket
import random
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '../primelib'))
from primesGenerator import PGenerator

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
            #Генерация большого простого числа
            pg = PGenerator()
            p = pg.nextPrime()
            A = pow(g, a, p)
            print(f"Генерация данных: \na = {a}\ng = {g}\np = {p}\nA = {A}")

            #Отправка сгенерированных данных второму клиенту
            print("Отправка собеседику: g, p, A")
            sock.sendall((str(g) + "\n" + str(p) + "\n" + str(A)).encode())
            print("Ожидание значения B от собеседника...")
            
            #Получение от второго клиента числа B, сгенерированного на основе отправленных данных
            B = int(sock.recv(1024).decode("utf-8"))
            print(f"От собеседника пришло B = {B}")

            #Генерация ключа K = B^a mod p
            K = pow(B, a, p)
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
            #B = g^b mod p
            B = pow(int(g), int(b), int(p))
            print(f"Генерирую B = g^b mod p = {B}")
            print("Отправляю сгенерированное значение В собеседнику")
            sock.sendall(str(B).encode())
            
            #Генерация ключа K = A^b mod p
            K = pow(int(A), int(b), int(p))
            print(f"Генерация общего секретного ключа: K = A^b mod p = {A}^{b} mod {p} = {K}")
