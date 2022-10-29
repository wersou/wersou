def BinarySearch(a, n):
    first = 0
    last = len(a) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if a[mid] == n:
            index = mid
        else:
            if n < a[mid]:
                last = mid - 1
            else:
                first = mid +1
    return index
print(BinarySearch([1,3,5,7,9], 7))


