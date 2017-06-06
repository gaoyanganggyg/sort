#!-*-coding:utf-8-*-


def s(d):
    """
    三、简单选择排序
    通过n-i次关键字之间的比较,从n-i+1 个记录中选择关键字最小的记录,并和第i(1<=i<=n)个记录交换之
    尽管与冒泡排序同为O(n^2),但简单选择排序的性能要略优于冒泡排序
    :return: 
    """
    l = len(d)
    for i in range(l):
        pos = i
        for j in range(i+1, l):
            if d[j] < d[pos]:
                pos = j
        d[i], d[pos] = d[pos], d[i]
    return d


if __name__ == '__main__':
    d = [3, 1, 5, 7, 2, 4, 9, 6]
    print s(d)
