from random import randint
a, b = [], []
for i in range(randint(1, 1000)):
    a.append(randint(1, 10000))
for i in range(randint(1, 1000)):
    b.append(randint(1, 10000))
def merge(a, b):
    res = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res += a[i:] + b[j:]
    return res
def MergeSort(a):
    if len(a) <= 1:
        return a
    else:
        l = a[:len(a) // 2]
        r = a[len(a) // 2:]
    return merge(MergeSort(l), MergeSort(r))
print(MergeSort(a))

