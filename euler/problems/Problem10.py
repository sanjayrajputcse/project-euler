# https://projecteuler.net/problem=10
# Que: Summation of primes
# Ans: 142913828922
from lib.Math import get_primes_between
sum = 0
for prime in get_primes_between(2, 2000000):
    sum += prime
print sum