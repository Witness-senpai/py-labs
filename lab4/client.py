import socket
import random
import string
import sys
import os
import hashlib as h

sys.path.append(os.path.join(os.path.dirname(__file__), '../primelib'))
from primesGenerator import PGenerator


# Генерация безопасного простого, 2*p + 1, где p - тоже простое, а также генерация g
def get_save_prime_g(bits=64):
    pg = PGenerator()
    save_prime = 2*pg.nextPrime(bits) + 1

    while (not pg.isPrime(save_prime)):
        save_prime = 2*pg.nextPrime(bits) + 1
    # Генератор по модулю save_prime
    g = 2

    return (save_prime, g)

def get_hash(s):
    return int(h.sha256(str(s).encode()).hexdigest(), base=16)

# Костыль
N = 21766174458617435773191008891802753781907668374255538511144643224689886235383840957210909013086056401571399717235807266581649606472148410291413364152197364477180887395655483738115072677402235101762521901569820740293149529620419333266262073471054548368736039519702486226506248861060256971802984953561121442680157668000761429988222457090413873973970171927093992114751765168063614761119615476233422096442783117971236371647333871414335895773474667308967050807005509320424799678417036867928316761272274230314067548291133582479583061439577559347101961771406173684378522703483495337037655006751328447510550299250924469288819
g = 2

sock = socket.socket()

# Клиент подключился к серверу
sock.connect((socket.gethostname(), 1234))
print("Добро пожаловать на сервер!")
way = -1
while way != 0:
    print("======================")
    print("1 - Зарегестрироваться")
    print("2 - Войти")
    print("0 - Закрыть программу")
    way = input(">> ")
    # Отправка запроса
    sock.sendall(way.encode())
    # Регистрация
    if way == '1':
        # Ввод логина и пароля для регистрации
        I = input("Логин: ")
        p = input("Пароль:")
        # Получение prime и g
        #N, g = get_save_prime_g(512)

        # Генерация соли
        s = ''.join((random.choice(string.ascii_letters)) for i in range(10))
        # Генерация x
        x = get_hash(s + p)
        # Генерация верификатора пароля
        v = pow(int(g), x, int(N))
        # Отправка серверу имени, соли, и верификатора
        sock.sendall(f"{I}\n{s}\n{v}".encode())
        print("Регистрация завершена.")
    elif (way == "2"): # Вход
        print("Вход на сервер для зарегестрированнх пользователей: ")
        # Ввод логина и пароля для входа
        I = input("Логин: ")
        p = input("Пароль:")

        # Генерация случайного числа а и A = g^a % N
        a = random.randint(1, 100)
        #N, g = get_save_prime_g(256)
        A = pow(g, a, N)

        # Отправка вычесленных выше данных серверу
        sock.sendall(f"{I}\n{A}\n{N}\n{g}".encode())

        # Получаем сразу ответ с солью и B
        B, s = sock.recv(1024).decode("utf-8").split('\n')
        if (B == '0' and s == '0'):
            print("Такого пользователя не существует!")
            continue

        # Вычислям скремблер(Сервер тоже)
        u = get_hash(str(A) + B)
        if u == 0:
            print("Ошибка: u == 0")
            break
        
        # Вычисления общего ключа сессии
        x = get_hash(s + p)
        # k = int(h.sha256((str(N) + str(g)).encode()).hexdigest(), base=16)
        k = get_hash(str(N) + str(g))
        S = pow(int(B) - k*pow(g, x, N), a + u*x, N)
        K = get_hash(str(S))
        #print(f"u = {u}\nk = {k}\nS = {S}\nK = {K}")

        # Генерация подтверждения для сервера 
        M = get_hash(
            str( get_hash(N) ^ get_hash(g) ) + \
            str(get_hash(I)) + s + str(A) + str(B) + str(K)
            )
        sock.sendall(str(M).encode())

        #print(M)

        # Повторная проверка кода со стороны сервера
        R = get_hash(str(A) + str(M) + str(K))
        R_from_server = sock.recv(1024).decode('utf-8')

        if (str(R) != R_from_server):
            print("Неверный пароль, попробуйте снова!")
            sock.close()
            continue
        print("Пароль подтверждён!")
    
    else:
        sock.close()
        print("Выход...")
        break
    
