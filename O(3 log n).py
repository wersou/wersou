from random import randint

a = []
for i in range(randint(1, 50)):
    a.append(randint(1, 100))
a.sort()
print(a)
isk = randint(1, 100)
print(isk)
mid = len(a) // 2
bot = 0
top = len(a) - 1
while a[mid] != isk and bot <= top:
    if isk > a[mid]:
        bot = mid + 1
    else:
        top = mid - 1
    mid = (bot + top) // 2
if bot > top:
    print('Такого числа в списке нет')
else:
    print('Номер в списке', mid)

