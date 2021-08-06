from itertools import count

my_list = [5, 5, 8, 10, 11, 8, 31, 89, 89, 26, 389, 524, 3, 3, 12, 389]
new_list = [i for i in my_list if my_list.count(i) == 1]
print(my_list)
print(new_list)
