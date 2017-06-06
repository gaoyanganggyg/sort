#!-*-coding:utf-8-*-


def s(data):
    """
    二、直接插入排序
    将一个记录插入到已经排好序的有序表中, 从而得到一个新的,记录数增1的有序表 
    时间复杂度也为O(n^2), 比冒泡法和选择排序的性能要更好一些
    """
    l = len(data)
    for i in range(1, l):
        t = data[i]
        f = i
        for j in range(i, 0, -1):
            if data[j - 1] > t:
                f = j - 1
                data[j] = data[j - 1]
            else:
                break
        data[f] = t
    return data


if __name__ == '__main__':
    d = [3, 1, 5, 7, 2, 4, 9, 6]
    print s(d)
