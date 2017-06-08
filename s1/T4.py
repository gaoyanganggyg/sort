#!-*-coding:utf-8-*-


def s(d, s):
    """
    希尔排序又叫缩小增量排序
    先将整个待排元素序列分割成若干子序列（由相隔某个“增量”的元素组成的）分别进行直接插入排序，然后依次缩减增量再进行排
    序，待整个序列中的元素基本有序（增量足够小）时，再对全体元素进行一次直接插入排序（增量为1）。其时间复杂度为O(n^3/2),要好于直接
    插入排序的O(n^2)
    :param d: 
    :param s: 
    :return: 
    """
    l = len(d)
    for i in range(s, l, s):
        t = d[i]
        pos = i
        for j in range(i, 0, -s):
            if d[j-s] > t:
                pos = j-s
                d[j] = d[j-s]
            else:
                break
        d[pos] = t
    return d


if __name__ == '__main__':
    d = [3, 1, 5, 7, 2, 4, 9, 6]
    for x in range(3, 0, -1):
        d = s(d, x)
        print d
