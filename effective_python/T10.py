
def t1():
    items = [('name', 'earth'), ('port', '80')]
    dict2 = dict(items)
    print dict2

    dict1 = dict((['name', 'earth'], ['port', '80']))
    print dict1


def t2():
    dict1 = {}.fromkeys(('x', 'y'), -1)
    print dict1
    dict2 = {}.fromkeys(('x', 'y'))
    print dict2

if __name__ == '__main__':
    t1()
    t2()
