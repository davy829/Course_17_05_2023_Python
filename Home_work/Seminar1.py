# Задача №1
# num = int(input('Введите любые четыре цифры получите сумму цифр_'))
# ln = str(num)
# res = 0
# for i in range(0, len(ln)):
#     res = res + num % 10
#     num = num // 10
# print(f"summ = {res} ")

# Задача №2
# num = int(input('Введите сколько всего журавлико _'))
# if num % 2 != 0:
#    num = num + 1
# petya = num / 4
# katya = num / 2
# serg = num / 4
# print(f"Катя сплела {int(katya)}шт")
# print(f"Петя сплел {int(petya)}шт")
# print(f"Серго сплел {int(serg)}шт")

# Задача №2
num = int(input('Введите номер билетика (6 цифр)_'))
firstNumer = num / 1000
secondNumber = num % 1000
summ1 = 0
summ2 = 0
for i in range(0, 3):
    summ1 = summ1 + firstNumer % 10
    firstNumer = firstNumer / 10
    summ2 = summ2 + secondNumber % 10
    secondNumber = secondNumber / 10
if summ1 == summ2:
    print(f"Your tiket is Happy {int(summ1)} + {int(summ2)}")
else:
    print(f"Your tiket is not Happy {int(summ1)} + {int(summ2)}")




