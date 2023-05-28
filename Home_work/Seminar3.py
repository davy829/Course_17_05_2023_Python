# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3 -> 1
# import random
#
# count = 0
# list_1 = []
# n = int(input("Count of element: "))
# for i in range(n):
#     mrnd = random.randint(11, 18)
#     list_1.insert(i, mrnd)
# print(list_1)
# x = int(input("what search ? : "))
# for i in list_1:
#     if i == x:
#         count = count + 1
# print(f"число {x} встречается {count} раз")

# -----------------------------------------------------------------------------------------------
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6 -> 5

# import random
#
# # dic = {'55': '50', '45': '5', '35': '30', '25': '20', '15': '10', '65': '60'}
# dic = {}
# min_1 = 80
# val_1 = 2
# n = int(input("Count of element: "))
# x = int(input("what search ? : "))
# for i in range(n):
#     mrnd = random.randint(9, 50)
#     dic[mrnd] = mrnd - x
#
# for (k, v) in dic.items():
#     print(f"key={k}. val={v}")
#     val_1 = int(v)
#     if 0 < val_1 < min_1:
#         min_1 = k
# print(f"min= {min_1}")

# -----------------------------------------------------------------------------------------------
# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# ang_dic = {'A': '1', 'E': '1', 'I': '1', 'O': '1', 'U': '1', 'L': '1', 'N': '1', 'S': '1', 'T': '1', 'R': '1',
#            'D': '2', 'G': '2', 'B': '3', 'C': '3', 'M': '3', 'P': '3',
#            'F': '4', 'H': '4', 'V': '4', 'W': '4', 'Y': '4', 'K': '5',
#            'J': '8', 'X': '8', 'Q': '10', 'Z': '10', 'a': '1', 'e': '1', 'i': '1', 'o': '1', 'u': '1', 'l': '1',
#            'n': '1', 's': '1', 't': '1', 'r': '1',
#            'd': '2', 'g': '2', 'b': '3', 'c': '3', 'm': '3', 'p': '3',
#            'f': '4', 'h': '4', 'v': '4', 'w': '4', 'y': '4', 'k': '5',
#            'j': '8', 'x': '8', 'q': '10', 'z': '10'}
# balls = 0
# word_user = input('Input a word : ')
# for i in range(len(word_user)):
#     for (k, v) in ang_dic.items():
#         if word_user[i] == k:
#             balls = balls + int(v)
# print(f"in word {word_user} are {balls} balls")

# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# rus_dic = {'А': '1', 'В': '1', 'Е': '1', 'И': '1', 'Н': '1', 'О': '1', 'Р': '1', 'С': '1', 'Т': '1',
#            'Д': '2', 'К': '2', 'Л': '2', 'М': '2', 'П': '2', 'У': '2',
#            'Б': '3', 'Г': '3', 'Ё': '3', 'Ь': '3', 'Я': '3',
#            'Й': '4', 'Ы': '4', 'Ж': '5', 'З': '5', 'Х': '5', 'Ц': '5', 'Ч': '5',
#            'Ш': '8', 'Э': '8', 'Ю': '8', 'Ф': '10', 'Ъ': '10',
#            'а': '1', 'в': '1', 'е': '1', 'и': '1', 'н': '1', 'о': '1', 'р': '1', 'с': '1', 'т': '1',
#            'д': '2', 'к': '2', 'л': '2', 'м': '2', 'п': '2', 'у': '2',
#            'б': '3', 'г': '3', 'ё': '3', 'ь': '3', 'я': '3',
#            'й': '4', 'ы': '4', 'ж': '5', 'з': '5', 'х': '5', 'ц': '5', 'ч': '5',
#            'ш': '8', 'э': '8', 'ю': '8', 'ф': '10'}
# balls = 0
# word_user = input('Input a word : ')
# for i in range(len(word_user)):
#     for (k, v) in rus_dic.items():
#         if word_user[i] == k:
#             balls = balls + int(v)
# print(f"in word {word_user} are {balls} balls")