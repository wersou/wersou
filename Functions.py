def QuickSort(a):
    if len(a) <= 1:
        return a
    else:
        mid = a[len(a) // 2]
    mina = [n for n in a if n < mid]
    mida = [mid] * a.count(mid)
    maxa = [n for n in a if n > mid]
    return QuickSort(mina) + mida + QuickSort(maxa)

def CombSort(a):
    step = len(a) // 2
    change = True
    while step > 1 or change:
        i = 0
        change = False
        while i + step < len(a):
            if a[i] > a[i + step]:
                a[i], a[i + step] = a[i + step], a[i]
                change = True
            i += 1
        if step > 1:
            step //= 2
    return a
