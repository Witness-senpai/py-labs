import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '../primelib'))
from primesGenerator import PGenerator

pg = PGenerator()

prime = pg.nextPrime(256)
while not pg.isPrime(2 * prime + 1):
    prime = pg.nextPrime(256)
safe_prime = 2 * prime + 1
print(f"prime: {prime} test: {pg.isPrime(prime)}")
print(f"prime: {safe_prime} test: {pg.isPrime(safe_prime)}")

