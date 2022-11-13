from random import randint

def QuickSort(buckets):
    if len(buckets) <= 1:
        return buckets
    else:
        mid = buckets[len(buckets) // 2]
    mina = [n for n in buckets if n < mid]
    mida = [mid] * buckets.count(mid)
    maxa = [n for n in buckets if n > mid]
    return QuickSort(mina) + mida + QuickSort(maxa)

def BucketSort(m):
    val = max(m)
    s = val / len(m)
    mas = []
    for x in range(len(m)):
        mas.append([])

    for i in range(len(m)):
        j = int(m[i] / s)
        if j != len(m):
            mas[j].append(m[i])
        else:
            mas[len(m) - 1].append(m[i])

    for y in range(len(m)):
        QuickSort(mas[y])

    b = []
    for x in range(len(m)):
        b = b + m[x]
    return b

a = []
n = randint(10, 50)
for i in range(n):
    a.append(randint(1,100))

print(a)
print(BucketSort(a))