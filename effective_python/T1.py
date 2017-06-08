#!-*-coding:utf-8-*-


class A:
    @classmethod
    def a(cls):
        print "aaa"

    @staticmethod
    def b():
        print "bbb"

    def c(self, *args, **kwargs):
        for x in args:
            print x

        for k, v in kwargs.iteritems():
            print k, v


if __name__ == '__main__':
    a = A()
    A.a()
    print getattr(A, "__name__")
    print isinstance(A, bytes)

    d = [1, 2, 3]
    b = {"s": 12, "c": 45}

    a.c(*d, **b)

