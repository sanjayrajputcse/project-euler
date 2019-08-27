# https://projecteuler.net/problem=12
# Que: Highly divisible triangular number
# Ans: 76576500
# Help : https://www.xarg.org/puzzle/project-euler/problem-12/
from lib.Math import sum_natural_numbers, get_first_n_primes_eval

primes = get_first_n_primes_eval(10000)
# print primes


def divisors(n):
    expo_sum = 1
    for prime in primes:
        if prime > n:
            break
        c = 1
        while (n % prime) == 0:
            c += 1
            n /= prime
        expo_sum *= c
    return expo_sum


i = 1
MAX_DIVISORS = 500
while True:
    n = sum_natural_numbers(i)
    divisors_count = divisors(n)
    print i, n, divisors_count
    if divisors_count > MAX_DIVISORS:
        break
    i += 1
