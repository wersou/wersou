from random import randint
import numpy as np
import matplotlib.pyplot as plt

n = randint(0, 50)
a = []
for i in range(n):
    a.append(randint(0, 100))
print('Список:', a)
mean = sum(a) / len(a)
print('Математическое ожидание =', mean)
s2n = sum((i - mean) ** 2 for i in a) / len(a)  # Смещенная выборочная дисперсия
s2 = len(a) * s2n / (len(a) - 1)  # Выборочная дисперсия
print('Среднеквадратическое отклонение =', s2n ** 0.5)  # Стандартное отклонение - корень из смещенной дисперсии

k = 0.5
b = 2
x = np.array(range(len(a)))
f = np.array([k*z+b for z in range(len(a))])
y = f + np.random.normal(0, mean, len(a))

mx = x.sum()/len(a)
my = y.sum()/len(a)
a2 = np.dot(x.T, x)/len(a)
a11 = np.dot(x.T, y)/len(a)

kk = (a11 - mx*my)/(a2 - mx**2)
bb = my - kk*mx
ff = np.array([kk*z+bb for z in range(len(a))])

plt.scatter(x, y, s=2, c='red')
plt.plot(f)
plt.plot(ff, c='green')
plt.grid(True)
plt.show()
