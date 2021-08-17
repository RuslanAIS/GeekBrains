# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.

f = open(r"C:\Users\r.tleugaliev\Desktop\GeekBrains\lessons 5\my_text2.txt", "w")
str_text = ['Купить зеленые яблоки в магазине зеленых яблок''\n''Купить апельсины в магазине апельсинов''\n']
f.writelines(str_text)
f.close()

with open('my_text2.txt') as r:
    line_count = 0
    for line in r:
        line_count += 1
print('Колличество строк в тексте: ', line_count)

with open('my_text2.txt') as r:
    for line in r.readlines():
        words: int = len(line.split())
        print('Колличество слов в строке: ', words)





