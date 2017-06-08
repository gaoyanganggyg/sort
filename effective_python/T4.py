#!-*-coding:utf-8-*-


def t1(fun):
    def wrapped(a1, a2):
        print a1, a2
        fun(a1, a2)
    return wrapped


@t1
def t2(a1, a2):
    print a2, a1

if __name__ == '__main__':
    t2("aa", "bb")
