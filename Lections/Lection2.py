#-------------------------------------------------------------------------------------------------
dictionary = {'one':'один','two':'два','three':'три','four':'четыре','five':'пять','six':'шесть'}
dictionary['seven'] = 'семь8'  # add in dictionary
del dictionary['two']          # delete key 'two'
# for item in dictionary:
#     print('{}:{}'.format(item,dictionary[item])) #output fomat
#     print(item)                              # output only keys

for (k,v) in dictionary.items():  # такой вывод еще
    print(v)
#-------------------------------------------------------------------------------------------------

# заполним список до 100 если ита четная
# list_1 = [i for i in range(1,101)]
# list_2 = [(i, i) for i in range(1,101)]
# list_3 = [(f'exp{i}',i) for i in range(1,101) if i % 2 == 0]
# list_4 = [(f'sqear_i_{i*2}',i) for i in range(1,101) if i % 2 == 0] # квадрат числа
# print(list_1)
