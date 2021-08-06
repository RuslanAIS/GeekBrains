my_list: list[int] = [289, 500, 21, 325, 5, 6, 381, 785, 24, 65, 25]
new_list = [x for i, x in enumerate(my_list) if i != 0 and my_list[i - 1] < my_list[i]]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")
