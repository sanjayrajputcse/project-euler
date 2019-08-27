def fibonacci(max):
    a, b = 1, 1
    while a < max:
        yield a
        a, b = b, a + b


def is_prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_factor(i, n):
    if n % i == 0:
        return True
    return False


def is_palindrome_number(n):
    rev = int(str(n)[::-1])
    if rev == n:
        return True
    return False


def generate_factors(n):
    i = 1
    while i <= n:
        if is_factor(i,n):
            yield i
        i += 1


def get_primes_between(a, b):
    for i in xrange(a, b):
        if is_prime(i):
            yield i


def get_first_n_primes_eval(n):
    prime_list = [2]
    i = 3
    while n > 1:
        is_prime_no  = True
        for p in prime_list:
            if (p * p) > i:
                break
            if (i % p) == 0:
                is_prime_no = False
                break
        if is_prime_no:
            prime_list.append(i)
            n -= 1
        i += 2
    return prime_list


def least_common_multipliers(n):
    i = 2
    while n > 1:
        c = 0
        while n % i == 0:
            n = n / i
            c += 1
        if c > 0:
            yield i, c
        i = i + 1


def sum_natural_numbers(n):
    return n * (n + 1) / 2


def sum_natural_number_squares(n):
    return n * (n + 1) * (2 * n + 1) / 6
