import timeit
import numpy as np
print('Возможные размеры матрицы: 3х3')
print('Введите количество строк исходной матрицы:')
n = int(input())
print('Введите данные исходной матрицы:')
A = []
for p in range(n):
    A.append(list(map(int, input().split())))
det = A[0][0]*A[1][1]*A[2][2]+A[0][1]*A[1][2]*A[2][0]+A[0][2]*A[1][0]*A[2][1]-A[0][2]*A[1][1]*A[2][0]-A[0][1]*A[1][0]*A[2][2]-A[0][0]*A[1][2]*A[2][1]
if det == 0:
    print('Детерминант равен нулю, обратной матрицы не существует.')
else:
    A1=np.linalg.inv(A)
    print('Обратная матрица:')
    print(A1)
print('Время выполнения программы:',timeit.timeit('output=10*5'))
