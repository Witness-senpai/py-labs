import random
import time
import math

#Генарация простых чисел с помощью теста Рабина-Мюллера
#В параметрах выбирается 
class primeGenerator():
    def __init__(self):
        self.prime = ''
    
    #Генерация случайного числа
    def __genRandNum(self, minBit, maxBit):
        x = ''
        #Генерация случайного большого числа
        for i in range(random.randint(minBit, maxBit)):
            x += str(random.randint(0, 1))

        #Принудительное добавление '1' в первый и последний разряды
        #Чтобы число точно было нечётное и без незначащих нулей в начале
        x = '1' + x[1:-1] + '1'

        return int(x, base=2)

    #ТестРабина-Мюллера
    def __RabinMillerTest(self):
        #Вычисление b - наибольшее кол-во целосисленных делений prime-1 на 2
        b = 0
        temp_prime = self.prime - 1
        while (temp_prime > 0):
            temp_prime /= 2
            if (temp_prime % 1 > 0): 
                break
            b += 1
        
        #Вычисление m такое, что prime - 1 = 2^b * m
        m = int( (self.prime - 1) / 2 ** b )

        #Количество раундов(шагов) берётся порядка log2(prime)
        for step in range(len(str(self.prime))):
            #Выбор случайного а из отрезка [2, prime-2]
            a = random.randint(2, self.prime - 2)

            #Вычисляем a ^ m mod prime
            z = pow(a, m, self.prime)
            #Prime скорее простое число
            if (z == 1 or z == self.prime - 1):
                continue
            
            #Внутренний цикл выполняется b-1 раз
            for i in range(b - 1):
                z = z * z % self.prime

                #Точно не простое число    
                if (z == 1):
                    return False

                #Вернуться к внешнему циклу
                if (z == self.prime - 1):      
                    break
            return False
        return True

    #minBit - минимальная длина в битах
    #maxBit - максимальная длина в битах
    def nextPrime(self, minBit=50, maxBit=100):
        #Пока не нашли простое число генерируем новое и проверяем его тестом
        while True:
            self.prime = self.__genRandNum(minBit, maxBit)
            if (self.__RabinMillerTest()):
                return self.prime

s = time.time()

pg = primeGenerator()
prime = pg.nextPrime()

print(f'Prime = {prime}, time = {time.time() - s}')