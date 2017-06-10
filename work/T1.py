#!-*-coding:utf-8-*-


def fun(arr, strs, l):
    if l >= len(arr):
        print strs
    else:
        for i in range(0, len(arr[l])):
            fun(arr, str(strs)+" "+str(arr[l][i]), l+1)

if __name__ == '__main__':
    arr = [[1, 3],
           [4, 2],
           [5, 8]]
    fun(arr, '', 0)

