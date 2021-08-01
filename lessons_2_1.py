enter_words = str(input('Введите любой текст:'))
x = enter_words.split()
y = 1
for i in x:
    print(y, i[:10])
    y += 1
