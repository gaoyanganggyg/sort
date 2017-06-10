#!-*-coding:utf-8-*-


def f1(n):
    if n <= 3:
        return n
    t = n / 2
    return f1(t) * f1(n - t)


def f2(n, re):
    if n == 0:
        print re
    else:
        for i in range(1, n+1):
            f2(n-i, str(re)+" "+str(i))


if __name__ == '__main__':
    # print f1(12)
    f2(4, "")
