print('PASSWORD')


def code():
    name = input('Введите имя: ')
    p = input('Введите пароль: ')
    if len(p) <= 8:
        print('Введите пароль больше <8> символов.')
        code()
    elif set(name) <= set(p):
        print('Пароль  не  должен содержать имя')
        code()

code()
print('OK PASSWORD')

