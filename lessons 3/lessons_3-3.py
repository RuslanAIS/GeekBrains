def my_func(x, y, z):
  if x >= y and y >= z:
    return x + y
  elif x <= y and y <= z:
    return y + z
  elif x >= z and y >= z:
    return x + y
  else:
    return x + z
print(f'Результат - {my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число:  ")))}')