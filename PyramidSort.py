from random import randint

def heaps(a, heap, ind):
    biggest = ind
    lef = 2 * ind + 1
    rig = 2 * ind + 2

    if lef < heap and a[ind] < a[lef]:
        biggest = lef

    if rig < heap and a[biggest] < a[rig]:
        biggest = rig

    if biggest != ind:
        a[ind], a[biggest] = a[biggest], a[ind]
        heaps(a, heap, biggest)

def PyramidSort(a):
    n = len(a)
    for i in range(n // 2, -1, -1):
        heaps(a, n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heaps(a, i, 0)
    return a

a = []
n = randint(10, 50)
for i in range(n):
    a.append(randint(1,100))

print(a)
print(PyramidSort(a))