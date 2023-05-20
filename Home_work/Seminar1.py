# Задача №1
# num = int(input('Введите любые четыре цифры получите сумму цифр_'))
# ln = str(num)
# res = 0
# for i in range(0, len(ln)):
#     res = res + num % 10
#     num = num // 10
# print(f"summ = {res} ")

# Задача №2
num = int(input('Введите сколько всего журавлико _'))
if num % 2 != 0:
   num = num + 1
petya = num / 4
katya = num / 2
serg = num / 4
print(f"Катя сплела {int(katya)}шт")
print(f"Петя сплел {int(petya)}шт")
print(f"Серго сплел {int(serg)}шт")