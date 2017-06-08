#!-*-coding:utf-8-*-


def t1(p="hello"):
    def t11(p):
        print p

    def t12(p):
        print p

    if "hello" == p:
        return t11
    else:
        return t12

if __name__ == '__main__':
    t1()("aaa")
