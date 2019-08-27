# https://projecteuler.net/problem=3
# Que: Largest prime factor
# Ans: 6857
from lib.Math import is_prime, is_factor
N = 600851475143


def gen_prime_factor(n):
    fact, max_fact = 2, 0
    while fact*fact <= n:
        # print str(fact) + "," + str(isFactor(fact, n)) + ", " + str(isPrime(fact))
        if is_factor(fact, n) & is_prime(fact):
            print fact
            max_fact = fact
        fact += 1
    return max_fact


print "max prime factorial : " + str(gen_prime_factor(N))