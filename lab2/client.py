import socket
import random

#некое множество простых чисел
simples = [3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517]
#Числа a, b, g генерируются случайно, p - простое число берётся из simples
#mod -> 0 - принимает g, p; 1 - генерирует g, p
a = b = g = p = mod = 0

name = input("Enter your name: ")
key = input("Do you want to generate starts values y/n?")

sock = socket.socket()
sock.connect((socket.gethostname(), 1234)) 

sock.sendall(bytes('hello, world!', 'utf-8'))

if 'y' in key:
    a = random.randint(100, 500)
    g = random.randint(10, 20)
    p = simples[random.randint(0, len(simples) - 1)]
    mod = 1
else:
    a = random.randint(100, 500)
    mod = 0

input()

msg = sock.recv(1024)
print(msg.decode('utf-8'))

#sock.close()