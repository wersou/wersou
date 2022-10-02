import numpy as np
print('Выберите операцию:\n'
      'Транспонирование матрицы (1)\n'
      'Умножение матриц (2)\n'
      'Определение ранга матрицы (3)\n')
action = input('Операция:')
if action in '1':
    print('Возможные размеры матрицы: 1х2, 2х1, 1х3, 3х1, 2х2, 3х3')
    print("Введите количество строк матрицы:")
    n = int(input())
    print('Введите данные матрицы:')
    A = []
    for p in range(n):
        A.append(list(map(int, input().split())))
    A_T=np.transpose(A)
    print('Транспонированная матрица\n', A_T)
elif action in '2':
    print('Возможные размеры матриц: 1х2, 2х1, 1х3, 3х1, 2х2, 3х3')
    print("Введите количество строк матрицы А:")
    n = int(input())
    print('Введите данные матрицы А:')
    A = []
    for p in range(n):
        A.append(list(map(int, input().split())))
    print("Введите количество строк матрицы B:\n"
          'Внимание! Количество столбцов матрицы А должно равняться количеству строк матрицы В')
    i = int(input())
    print('Введите данные матрицы B:')
    B = []
    for m in range(i):
        B.append(list(map(int, input().split())))
    print("Результат:")
    print(np.dot(A,B))
elif action in '3':
    print('Возможные размеры матрицы: 2х2, 3х3')
    print("Введите количество строк матрицы:")
    n = int(input())
    print('Введите данные матрицы:')
    A = []
    for p in range(n):
        A.append(list(map(int, input().split())))
    A_R=np.linalg.matrix_rank(A)
    print('Ранг матрицы:', A_R)

