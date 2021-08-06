def sal():
    try:
        time = float(input("Введите время в часах: "))
        salary = int(input('Введите ставку в тенге: '))
        bonus = int(input('Введите премию в тенге: '))
        res = time * salary + bonus
        print(f"Заработная плата сотрудника:  {res}")
    except ValueError:
        return print('Не правильно введены данные')
sal()


