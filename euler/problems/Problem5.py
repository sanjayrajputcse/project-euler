# https://projecteuler.net/problem=5
# Que: Smallest multiple
# Ans: 232792560
from lib.Math import get_primes_between, least_common_multipliers
a = 2
b = 20
mul = 1
for prime in get_primes_between(a, b):
    max = 0
    for i in xrange(a, b):
        lcm = list(least_common_multipliers(i))
        for item in lcm:
            if item[0] == prime:
                if max < item[1]:
                    max = item[1]
    if max > 0:
        mul *= pow(prime, max)
print mul
