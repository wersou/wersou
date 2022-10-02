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
    A_T = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    print('Транспонированная матрица:\n', A_T)
elif action in '2':
    print('Возможные размеры матриц: 1х2, 2х1, 1х3, 3х1, 2х2, 3х3')
    print("Введите количество строк матрицы А:")
    n = int(input())
    print('Введите данные матрицы А:')
    A = []
    for p in range(n):
        A.append(list(map(int, input().split())))
    print("Введите количество строк матрицы B:")
    i = int(input())
    print('Введите данные матрицы B:\n'
          'Внимание! Количество столбцов матрицы А должно равняться количеству строк матрицы В')
    B = []
    for m in range(i):
        B.append(list(map(int, input().split())))
    print('Результат:')
    length = len(A)
    result = [[0 for v in range(length)] for c in range(length)]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    for r in result:
        print(r)
elif action in '3':
    print('Возможные размеры матрицы: 2х2, 3х3')
    print("Введите количество строк матрицы:")
    n = int(input())
    print('Введите данные матрицы:')
    A = []
    for p in range(n):
        A.append(list(map(int, input().split())))
    if n == 2:
        if A[0].count(0) == 2 and A[1].count(0) == 2:
            print('Ранг матрицы равен 0')
        elif A[0].count(0) == 2:
            print('Ранг матрицы равен 1')
        elif A[1].count(0) == 2:
            print('Ранг матрицы равен 1')
        else:
            print('Ранг матрицы равен 2')
    elif n == 3:
        if A[0].count(0) == 3 and A[1].count(0) == 3 and A[2].count(0) == 3:
            print('Ранг матрицы равен 0')
        elif (A[0].count(0) == 3 and A[1].count(0) == 3) or \
                (A[0].count(0) == 3 and A[2].count(0) == 3) or \
                (A[2].count(0) == 3 and A[1].count(0) == 3):
            print('Ранг матрицы равен 1')
        elif (A[1].count(0) == 2 and A[0].count(0) != 3 and A[2].count(0) != 3) or \
                (A[0].count(0) == 2 and A[1].count(0) != 3 and A[2].count(0) != 3) or \
                (A[2].count(0) == 2 and A[0].count(0) != 3 and A[1].count(0) != 3):
            print('Ранг матрицы равен 2')
        else:
            print('Ранг матрицы равен 3')
