# https://projecteuler.net/problem=6
# Que: Sum square difference
# Ans: 25164150
from lib.Math import *
n = 100
sum_of_no = sum_natural_numbers(n)
sum_sq = sum_of_no * sum_of_no
sq_sum = sum_natural_number_squares(n)
print sum_of_no, sq_sum, sum_sq, (sum_sq-sq_sum)
