# https://projecteuler.net/problem=7
# Que: 10001st prime
# Ans: 104743
from lib.Math import *
primes = [2]
pCount = 1
n = 3
C = 10000
while True:
    is_prime = True
    for p in primes:
        if is_factor(p, n):
            is_prime = False
            break
        if (p * p) > n:
            break
    if is_prime:
        primes += [n]
        pCount += 1
        print pCount, n
    n += 1
    if C < pCount:
        break

