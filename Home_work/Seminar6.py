# Задача 30:
# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n = a1 + (n-1) * d.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
# -------------------R1---------------------------
# list_1 = []
# first_element = int(input('input first element: '))
# step_element = int(input('input step element: '))
# count_element = int(input('input count element: '))
# for i in range(first_element, count_element + 1, step_element):
#     list_1.append(i)
# print(*list_1)


# -----------------------------------------------------
# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
# ------------------------------------------------------
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9,
          0, -5, -5, 7]
list_res = []
from_value = int(input('input from : '))
end_value = int(input('input end : '))
for i in range(len(list_1)):
    if list_1[i] >= from_value and list_1[i] <= end_value:
        list_res.append(f"index_{i},")
print(*list_res)
