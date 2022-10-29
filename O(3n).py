from random import randint

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
x, b = 0, 0
for i in range(len(a)):
    x = a[randint(0, 14)]
    b = a[randint(0, 14)]
    y = x + b
print(y)
