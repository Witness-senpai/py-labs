import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '../primelib'))
from primesGenerator import PGenerator


# Расширенный алгоритм Евклида
def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


# Нахождение модульной инверсии, что и нужно для нахождения d(секретной экспоненты)
def mulinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b


# Посимвольная кодировка строки
def encrypt(data, PK):
    return [pow(ord(el), PK[0], PK[1]) for el in data]


# Посимволная расшифровка и соединение в строку
def decrypt(data, SK):
    return ''.join(chr(pow(el, SK[0], SK[1])) for el in data)


print(mulinv(1, 14))

""" 
Реализация протокола RSA
"""

# p и q - большие простые числа
pg = PGenerator()
p = pg.nextPrime(512)
q = pg.nextPrime(512)

# Получение 'модуля'
n = p * q

# Получение значение функции Эйлера
fi = (p - 1) * (q - 1)

# Генерация e (открытая экспонента), 1 < e < fi; должно быть простым и небольшим
e = pg.nextPrime(16)

# Вычисление d (закрытая экспонента)
d = mulinv(e, fi)

# Пара (e, n) - открытый ключ
PK = (e, n)
# Пара (d, n) - закрытый ключ
SK = (d, n)

"""
Шифровка - расшифровка
"""

# Входные данные
indata = input("Введите данные: ")

# Зашифрованный текст на основе публичного ключа
encryptText = encrypt(indata, PK)

print(f"Зашифрованное сообщение: {encryptText}")

# Расшифрованный текст на основе секретного ключа
decryptText = decrypt(encryptText, SK)

print(f"Расшифрованное сообщение: {decryptText}")
