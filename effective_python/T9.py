#!-*-coding:utf-8-*-


def t1(n):
    fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
    print fib(n)


def t2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    print b


def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def t3(n):
    if n < 2:
        return 1
    return t3(n-1) + t3(n-2)


def t4(n):
    fib = lambda n: n if n < 2 else 2 * fib(n - 1)
    print fib(n)

if __name__ == '__main__':
    t1(3)
    t2(3)
    print t3(3)
    t4(100)
