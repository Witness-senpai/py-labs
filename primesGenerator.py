import random

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
        x = '1' + x[1:-1] + '1'

        return int(x, base=2)

    #ТестРабина-Мюллера
    def __RabinMillerTest(self):
        #Вычисление b - наибольшее кол-во делений prime-1 на 2
        b = 0
        temp_prime = self.prime - 1
        while (temp_prime > 0):
            temp_prime /= 2
            if (temp_prime % 1 > 0): 
                break
            b += 1
        
        #Вычисление m такое, что prime = 1 + 2^b * m
        m = int( (self.prime - 1) / 2 ** b )

        #Выбор случайного а, при условии а < prime
        a = random.randint(1, 100)

        j = 0
        z = a ** m % self.prime
        #Prime скорее простое число
        if (z == 1 or z == self.prime - 1):
            return self.prime

        while(True):
            #Prime точно не простое число    
            if (j > 0 and z == 1):
                return -1

            j += 1
            if (j < b and z < self.prime - 1):
                z = z * z % self.prime
                continue

            #Prime скорее всего простое число
            if (z == self.prime - 1):
                return self.prime
            #Prime точно не простое число
            if (j == b and z != self.prime - 1):
                return -1

    #minBit - минимальная длина в битах
    #maxBit - максимальная длина в битах
    def getPrime(self, minBit=30, maxBit=60):
        #Пока не нашли простое число генерируем новое и проверяем его тестом
        while True:
           # self.prime = self.__genRandNum(minBit, maxBit)
            self.prime = 5998757
            if (self.__RabinMillerTest()):
                return self.prime

pg = primeGenerator()
prime = pg.getPrime()
print(prime)
