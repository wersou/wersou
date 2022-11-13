from Functions import QuickSort
from Functions import CombSort
from random import randint
import timeit

a = []
n = randint(10, 50)
for i in range(n):
    a.append(randint(1,100))

print('Выберите метод сортировки\n'
      'Быстрая сортировка (1)\n'
      'Сортировка расчёской (2)')

k = int(input())
print(a)
if k == 1:
    print(QuickSort(a))
    print('Время: ', timeit.timeit('output=10*5'))
elif k == 2:
    print(CombSort(a))
    print('Время: ', timeit.timeit('output=10*5'))