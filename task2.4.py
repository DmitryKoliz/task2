#Задача 4. Необходимо определить индексы первого и последнего вхождения символа в строке. 
list = ['a', 'b', 'c', 'd', 'a', 'c', '1', '2', 'a']
fist_index = list.index('c')
last_index = list[::-1].index('a')
last_index = len(list)
print('Fist index:  ', fist_index, 'Last index:  ', last_index)

