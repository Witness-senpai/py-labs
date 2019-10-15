import socket
import hashlib
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../primelib'))
from primesGenerator import PGenerator

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(1)

print("Сервер запущен. Ожидание клиентов")

pg = PGenerator()
# Генерация безопасного простого, 2*p + 1, где p - тоже простое
save_prime = 2*pg.nextPrime(64) + 1
while (not pg.isPrime(save_prime)):
    save_prime = 2*pg.nextPrime(64) + 1
N = save_prime
# Генератор по модулю save_prime
g = 2
# Параметр-множитель
k = hash(save_prime ^ g)
    
while True:
    # Когда клиент подключится
    addr, port = s.accept()

    way = addr.recv(1024).decode("utf-8")

    # Регистрация
    if way == "1":
        # Отправка простого числа и g
        addr.send((f"{N}\n{g}").encode())
        
        # Получение username, salt, password
        I, s, v = addr.recv(1024).decode("utf-8").split('\n')

        # Запись в БД полученных данных
        with open("lab4/bd.txt", "w") as f:
            f.write(f"{I};{s};{v}")

    else: # Вход
        pass






def register():
    pass

def login():
    pass


    

