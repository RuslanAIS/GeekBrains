def my_sum():
    x = False
    sum_ = 0
    while x == False:
        number = input('Введите числа через проблел и Q чтобы закончить программу: ').split()
        z = 0
        for y in range(len(number)):
            if number[y] == 'q' or number[y] == 'Q':
                x = True
                break
            else:
                z = z + int(number[y])
        sum_ = sum_ + z
        print(f'Сумма введенных числе составляет: {sum_}')
    print(f'Общая сумма введеных числе составляет: {sum_}')
my_sum()
