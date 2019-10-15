import socket
import hashlib
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../primelib'))
from primesGenerator import PGenerator

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(socket.gethostname(), 1234)
s.listen(1)

print("Сервер запущен")

pg = PGenerator()
# Генерация безопасного простого, 2*p + 1, где p - тоже простое
save_prime = 2*pg.nextPrime(256) + 1
while (not pg.isPrime(save_prime)):
    save_prime = 2*pg.nextPrime(256) + 1
    
while True:
    # Когда клиент подключится
    addr, port = s.accept()


    


    

