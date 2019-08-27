# https://projecteuler.net/problem=2
# Que: Even Fibonacci numbers
# Ans : 4613732
from lib.Math import fibonacci
MAX_FIBO_NO = 4000000


def even_fibonacci(n):
    gen = list(fibonacci(n))
    c = 0
    for e in gen:
        if e % 2 == 0:
            print e
            c += e
    return c


print "sum of even fibonacci : " + str(even_fibonacci(MAX_FIBO_NO))