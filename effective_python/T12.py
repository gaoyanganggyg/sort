
def qsort(seq):
    if seq == []:
        return []
    else:
        pivot = seq[0]
        lesser = qsort([x for x in seq[1:] if x < pivot])
        greater = qsort([x for x in seq[1:] if x >= pivot])
        return lesser+[pivot]+greater


def qsort2(a, l, r, i):
    if l >= r:
        return
    pivot = a[i]
    a[i], a[r-1] = a[r-1], a[i]
    store_index = l
    for x in range(l, r):
        if a[x] < pivot:
            a[x], a[store_index] = a[store_index], a[x]
            store_index += 1
    a[store_index], a[r-1] = a[r-1], a[store_index]

    qsort2(a, l, store_index, l)
    qsort2(a, store_index+1, r, store_index+1)

if __name__ == '__main__':
    seq = [5, 6, 78, 9, 0, -1, 2, 3, -65, 12]
    # print(qsort(seq))

    qsort2(seq, 0, len(seq), 0)
    print seq

