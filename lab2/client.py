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
    print(name + ": отправка a, g, p, A собеседнику: " + 
        str(a) + "\n" + \
        str(g) + "\n" + \
        str(p) + "\n" + \
        str((g ** a) % p))
    #Отправка сгенерированных данных второму клиенту
    sock.sendall((name + '\n' + \
                str(a) + "\n" + \
                str(g) + "\n" + \
                str(p) + "\n" + \
                str((g ** a) % p)).encode())
    print(name + ": ожидаю значение B от собеседника...")
    
    #Получение от второго клиента числа B, сгенерированного на основе отправленных данных
    B = int(sock.recv(1024).decode("utf-8"))
    print("От собеседника пришло B = " + str(B))

    #Генерация ключа
    K = B ** a % p
    print("Ключ : " + str(K))

else:
    b = random.randint(100, 500)
    print(name + ": ожидаю b, g, p, A...")
    #Получение сгенерированных данных
    msg = sock.recv(1024).decode("utf-8").split('\n')
    a = msg[0]
    g = msg[1]
    p = msg[2]
    A = msg[3]
    print("От собеседника пришло: \na = " + str(a) + \
        "\ng = " + str(g) + "\np = " + str(p) + "\nA = " + str(A))
    #Формирование на их основе ещё одного числа и его отправка
    B = (int(g) ** int(b)) % int(p)
    print(name + ": генерация B = g ^ b mod p = " + str(B))
    print(name + ": отправка В собеседнику")
    sock.sendall(str(B).encode())
    
    #Генерация ключа
    K = int(A) ** int(b) % int(p)
    print("Ключ : " + str(K))

input()

msg = sock.recv(1024)
print(msg.decode('utf-8'))

sock.close()

def generate_key(A, b, p):
    return A ** b % p