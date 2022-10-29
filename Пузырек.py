from random import randint
import time
print('Введите длину массива:')
N = int(input())
a = []
for i in range(N):
    a.append(randint(1,10000))
print(a)
print('Сортировка пузырьком')
start = time.time()
for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(time.time()-start)
print(a)

print('Сортировка')
start1 = time.time()
a.sort()
print(time.time()-start1)
print(a)
