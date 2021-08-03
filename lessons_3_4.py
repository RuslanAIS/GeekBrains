def my_func(x, y):
    return 1 / x ** abs(y)
print(f'Результат - {my_func(int(input("Введите число: ")), int(input("Введите отрицательное число, для возведения в степень: ")))}')