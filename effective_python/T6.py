#!-*-coding:utf-8-*-


def t1(arg):
    print arg

    def wrapped(fun):
        print "a fun"

        def wrapped1(a, b):
            fun(a, b)
        return wrapped1
    return wrapped


@t1("h1")
def t2(a, b):
    print a, b


if __name__ == '__main__':
    t2("x", "c")
