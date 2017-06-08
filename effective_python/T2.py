#!-*-coding:utf-8-*-


def t1(fn):
    def wrapped():
        return "<a>" + fn() + "</a>"
    return wrapped


def t2(fn):
    def wrapped():
        return "<p>" + fn() + "</p>"
    return wrapped


@t1
@t2
def t3():
    return "Hello"

if __name__ == '__main__':
    print t3()
