while True:
    a = float(input('Число:\n'))
    b = input('Знак:\n')
    c = float(input('Процент:\n'))

    if b == '+':
        print('Результат:\n' + str(a + a / 100 * c))
        print('В плюс на:\n' + str(a / 100 * c))
    elif b == '-':
        print('Результат:\n' + str(a - a / 100 * c))
        print('В минус на:\n' + str(a / 100 * c))
    elif b == str():
        print('Ошибка!!!')
        pass
    else:
        print('Ошибка!!!')
        pass
    d = input("Выход?\n+/-:\n")
    if d == "+":
        exit()
    elif d == "-":
        a = float(input('Число:\n'))
        b = input('Знак:\n')
        c = float(input('Процент:\n'))

        if b == '+':
            print('Результат:\n' + str(a + a / 100 * c))
            print('В плюс на:\n' + str(a / 100 * c))
        elif b == '-':
            print('Результат:\n' + str(a - a / 100 * c))
            print('В минус на:\n' + str(a / 100 * c))
        elif b == str():
            print('Ошибка!!!')
            pass
        else:
            print('Ошибка!!!')
            pass
