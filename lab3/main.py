import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '../primelib'))
from primesGenerator import PGenerator

""" 
Реализация протокола RSA
"""
# Расширенный алгоритм Евклида
def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

# Нахождениямодульной инверсии, что и нужно для нахождения d(секретной экспоненты)
def mulinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b

# p и q - большие простые числа
pg = PGenerator()
p = pg.nextPrime(64)
q = pg.nextPrime(64)

# Получение 'модуля'
n = p * q

# Получение значение функции Эйлера
fi = (p - 1) * (q - 1)

# Генерация e (открытая экспонента), 1 < e < fi; должно быть простым и небольшим
e = 65537

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
idata = int(input("Введите данные: "))

# Зашифрованный текст на основе публичного ключа
encryptText = pow(idata, PK[0], PK[1])

print(f"Зашифрованное сообщение: {encryptText}")

# Расшифрованный текст на основе секретного ключа
decryptText = pow(encryptText, SK[0], SK[1])

print(f"Расшифрованное сообщение: {decryptText}")