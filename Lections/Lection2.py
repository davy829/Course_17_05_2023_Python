#-------------------------------------------------------------------------------------------------
dictionary = {'one':'один','two':'два','three':'три','four':'четыре','five':'пять','six':'шесть'}
dictionary['seven'] = 'семь8'  # add in dictionary
del dictionary['two']          # delete key 'two'
for item in dictionary:
    print('{}:{}'.format(item,dictionary[item]))
#-------------------------------------------------------------------------------------------------