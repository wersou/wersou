import math


def pr(n):
    while not (n.replace('.', '', 1).isdigit() or n.replace('-', ' ', 1).isdigit()):
        n = input('Введенный элемент не является числом. Повторите ввод: ')
    return float(n)


def main():
    while True:
        print("Выберите необходимую функцию:\n"
              "Выход\n"
              "Сложение\n"
              "Вычитане\n"
              "Умножение\n"
              "Деление\n"
              "Возведение в степень\n"
              "Логарифм\n"
              "Округление в большую\n"
              "Округление в меньшую\n"
              "Округление до N знака после запятой\n")
        action = input("Функция: ")
        if action == "Выход":
            print("Выход из программы")
            break
        if action in ('Сложение', 'Вычитание', 'Умножение', 'Деление', 'Возведение в степень', 'Логарифм',
                      'Округление до N знака после запятой'):
            print("Введите первый элемент:")
            x = pr(input())
            print("Введите второй элемент:")
            y = pr(input())
            if action == 'Сложение':
                print('%.2f + %.2f = %.2f' % (x, y, x + y))
            elif action == 'Вычитание':
                print('%.2f - %.2f = %.2f' % (x, y, x - y))
            elif action == 'Умножение':
                print('%.2f * %.2f = %.2f' % (x, y, x * y))
            elif action == 'Деление':
                if y != 0:
                    print('%.2f / %.2f = %.2f' % (x, y, x / y))
                else:
                    print("Деление на ноль!")
            elif action == 'Возведение в степень':
                print('%.2f**%.2f = %.2f' % (x, y, x ** y))
            elif action == 'Логарифм':
                print('Аргумент: %.2f\n'
                      'Основание: %.2f\n'
                      'Логарифм: %.2f' % (x, y, math.log(x, y)))
            elif action == 'Округление до N знака после запятой':
                print(round(x, int(y)))
        elif action in ('Округление в большую', 'Округление в меньшую'):
            print("Введите элемент для округления:")
            x = pr(input())
            if action == 'Округление в большую':
                print(math.ceil(x))
            elif action == 'Округление в меньшую':
                print(math.floor(x))


if __name__ == '__main__':
    main()
