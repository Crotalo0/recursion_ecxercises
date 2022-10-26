import timeit
from functools import cache
# Example of how slow can be recursion
# And how cache decorator can optimize drastically recursion speed

def main():
    lista = []
    for i in range(1, 35):
        lista.append(fibonacci_iter(i))
    print(lista)


def fib_yield(n_series):
    """Generator for fib_array"""
    total = 0
    a, b = 0, 1
    while total < n_series:
        yield a
        c = a + b
        a = b
        b = c
        total += 1


def fibonacci_iter(n):
    a, b = 0, 1
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    while n - 2 != 0:
        c = a + b
        a = b
        b = c
        n = n - 1
    return c

@cache
def fibonacci_rec(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


if __name__ == "__main__":

    print(timeit.timeit(stmt='fibonacci_iter(1000)', setup='from __main__ import fibonacci_iter', number=1))
    print(timeit.timeit(stmt='fibonacci_rec(1000)', setup='from __main__ import fibonacci_rec', number=1))
    for i in fib_yield(20):
        print(i)
