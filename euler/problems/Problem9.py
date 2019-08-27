# https://projecteuler.net/problem=9
# Que: Special Pythagorean triplet
# Ans: 31875000
# a^2+b^2=c^2
# a+b+c=1000
# a^2+b^2=(1000-a-b)^2
for a in range(1000):
    for b in range(1000):
        exp = (1000-a-b)*(1000-a-b)-(a*a)-(b*b)
        if exp == 0:
            c = 1000-a-b
            print a,b,c,a*b*c