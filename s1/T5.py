#!-*-coding:utf-8-*-


def s(d):
    """
    简单选择排序的改进——二元选择排序
    简单选择排序，每趟循环只能确定一个元素排序后的定位。我们可以考虑改进为每趟循环确定两个元素
    （当前趟最大和最小记录）的位置,从而减少排序所需的循环次数。改进后对n个数据进行排序，最多只需进行[n/2]趟循环即可。
    :param d: 
    :return: 
    """
    l = len(d)
    for i in range(l/2):
        max_pos = l - i - 1
        min, max = i, i
        for j in range(i+1, l-i):
            if d[j] < d[min]:
                min = j
            if d[j] > d[max]:
                max = j
        d[i], d[min] = d[min], d[i]
        d[max_pos], d[max] = d[max], d[max_pos]
    return d

if __name__ == '__main__':
    d = [3, 1, 5, 7, 2, 4, 9, 6]
    print s(d)