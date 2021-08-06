from itertools import count
from itertools import cycle

for x in count(int(input('Введите целое число: '))):
    if x == 100:
        break
    print(x)

my_list = ['Ruslan', 'Alexey', 'Vovan', 'Nilolay', 'Sasha']
y = 0
for el in cycle(my_list):
    if y == 10:
        break
    print(el)
    y += 1
