#!-*-coding:utf-8-*-


class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(A, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    pass