# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# n = int(input('Введите любое число'))
# composition_number = 1
# if n < 0:
#     n = n - n - n
# i = 0
# while i < n:
#     i = i + 1
#     composition_number = composition_number * i
#     if i == n:
#         print(f"от 0 до {i} произведение равно {composition_number}")
#         break
#--------------------------------------------------------------------------------------------------------------

# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# a = int(input('Введите число больше нуля: '))
# n = 13
# f1 = f2 = 1
# # print(f1, f2, end='-')
# count = 3
# place = 0
# for i in range(2, n):
# 	f1, f2 = f2, f1 + f2
# 	# print(f2, end='-')
# 	count = count + 1
# 	if a == f2:
# 		place = count
# if place > 0:
# 	print(f"{a} находиться на {place} месте в ряду Фибоначи")
# else:
# 	print("-1")
#----------------------------------------------------------------------------------------------------------
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# dayT = int(input('Введите сколько дней просчитать : '))
# count = 0
# maxT = 0
# for i in range(dayT):
# 	temp = int(input(f"Введите температуру {dayT} раз: "))
# 	if temp > 0:
# 		count = count + 1
# 	else:
# 		if count > maxT:
# 			maxT = count
# 			count = 0
#
#
# print(f"{maxT} дней подряд плюсовая температура")
#-------------------------------------------------------------------------------------------------------------------
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

arbuzCount = int(input("Введите количество арбузов:"))
vesarb = 0
minArb = 100
maxArb = 0
for i in range(arbuzCount):
    vesarb = int(input("Введите веса арбузов:"))
    if vesarb > maxArb:
        maxArb = vesarb
    if vesarb < minArb:
        minArb = vesarb

print(f"Cамый легкий арбуз {minArb}кг. \n Cамый тяжелый арбуз {maxArb}кг")





