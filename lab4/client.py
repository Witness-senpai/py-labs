import socket
import random
import string

sock = socket.socket()

# Клиент подключился к серверу
sock.connect((socket.gethostname(), 1234))
while True:
    print("Добро пожаловать на сервер!")
    print("1 - Зарегестрироваться")
    print("2 - Войти")
    way = input(">> ")
    # Отправка запроса
    sock.sendall(way.encode())

    # Регистрация
    if way == '1':
        # Ввод логина и пароля для регистрации
        I = input("Логин: ")
        p = input("Пароль:")

        # Получение от сервера prime и g
        N, g = sock.recv(1024).decode('utf-8').split('\n')

        # Генерация соли
        s = ''.join((random.choice(string.ascii_letters)) for i in range(10))

        # Генерация x
        x = hash(s + p)

        # Генерация верификатора пароля
        v = pow(int(g), x, int(N))

        # Отправка серверу имени, соли, и верификатора
        sock.sendall(f"{I}\n{s}\n{v}".encode())
    else: # Вход
        print("Вход на сервер для зарегестрированнх пользователей: ")
        # Ввод логина и пароля для входа
        I = input("Логин: ")
        p = input("Пароль:")
        sock.recv(1024).decode('utf-8')
    