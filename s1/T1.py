#!-*-coding:utf-8-*-


def s(data):
    """
    冒泡排序
    基本思想是:两两比较相邻记录的关键字,如果反序则交换
    冒泡排序时间复杂度最好的情况为O(n),最坏的情况是O(n^2) 

    改进思路1：设置标志位，明显如果有一趟没有发生交换（flag = false)，说明排序已经完成
    :param data: 
    :return: 
    """
    l = len(data)
    for i in range(l):
        flag = True
        for j in range(l - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                flag = False
        if flag:
            break
    return data


if __name__ == '__main__':
    d = [3, 1, 5, 7, 2, 4, 9, 6]
    print s(d)
