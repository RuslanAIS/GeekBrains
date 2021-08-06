def my_func():
    try:
        x = int(input('Введите делимое:'))
        y = int(input('Введите делитель:'))
    except ValueError:
        return
    if y == 0:
        print('На ноль делить нельзя!')
    else:
        s_full = x/y
        return s_full
print(my_func())