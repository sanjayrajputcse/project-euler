# https://projecteuler.net/problem=4
# Que: Largest palindrome product
# Ans: 906609
from lib.Math import is_palindrome_number
max_palindrome = 0
for i in xrange(100, 999):
    for j in xrange(100, 999):
        product = i * j
        if is_palindrome_number(product) & (max_palindrome < product):
            max_palindrome = product
print max_palindrome
