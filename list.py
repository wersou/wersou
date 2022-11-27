from random import randint

print("Введите количесвто элементов в списке:")
n = int(input())

print("Список:")
a = []
for i in range(n):
    a.append(randint(0, 1))
print(a)

for i in range(1, n+1):
    nol = 0
    for j in range(0, n - i + 1):
        if sum(a[j:j + i]) == 0:
            nol += 1
    nol = nol / (n-i+1)
    ed = 0
    for y in range(0, n - i + 1):
        if sum(a[y:y + i]) == i:
            ed += 1
    ed = ed / (n-i+1)
    if nol == ed == 0:
        break
    print("Вероятность", i*"0", ":", round((nol * 100), 2), "%")
    print("Вероятность", i*"1", ":", round((ed * 100), 2), "%")