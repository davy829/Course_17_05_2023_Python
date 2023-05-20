# Задача №1
num = int(input('Введите любые четыре цифры получите сумму цифр_'))
ln = str(num)
res = 0
for i in range(0, len(ln)):
    res = res + num % 10
    num = num // 10
print(f"summ = {res} ")
