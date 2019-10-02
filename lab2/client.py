import socket
import random

#некое множество простых чисел
simples = [3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517]
#Числа a, b, g генерируются случайно, p - простое число берётся из simples

name = input("Enter your name: ")
key = input("Do you want to generate starts values y/n?")

sock = socket.socket()
sock.connect((socket.gethostname(), 3125)) 

if 'y' in key:
    a = random.randint(100, 500)
    g = random.randint(10, 20)
    p = simples[random.randint(0, len(simples) - 1)]
    
    #Отправка основных данных второму клиенту
    sock.sendall((name + ': send values a, g, p, A: \n' + \
                str(a) + "\n" + \
                str(g) + "\n" + \
                str(p) + "\n" + \
                str((g ** a) % p)).encode())
    
    
else:
    a = random.randint(100, 500)
    print(name + ": ожидаю получения a, g, p,")

    #sock.sendall((name + ': жду данные').encode())

input()

msg = sock.recv(1024)
print(msg.decode('utf-8'))

sock.close()