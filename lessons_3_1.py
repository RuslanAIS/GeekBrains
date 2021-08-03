def my_func(name, surname, birth, city, email, tel):
    name = str(input('Введите имя:'))
    surname = str(input('Введите фамилию:'))
    birth = int(input('Введите год рождения:'))
    city = str(input('Введите город проживания:'))
    email = str(input('Введите электронный адрес:'))
    tel = int(input('Введите телефон:'))
    return(name, surname, birth, city, email, tel)
print(my_func('name', 'surname', 'birth', 'city', 'email', 'tel'))