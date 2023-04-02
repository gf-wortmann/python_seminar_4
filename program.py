# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы
# множеств
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Условия задачи слегка расширены: можно ввести длины произвольного количества массивов.
# Результатом будет пересечение ВСЕХ массивов.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


from random import randrange
# getting user's input
list_length = [int(i) for i in input('Enter lengths of any arrays: ').split()]

# forming random lists of integers
# upper margin at 100 set just for simplicity
lists = [
        [randrange(1,100) for j in range(list_length[i])]
         for i in range(len(list_length))
        ]

# forming sets of unique values of the lists
sets = [set(lists[i]) for i in range(len(list_length))]

# getting intersection of all sets
res = set(sets[0])  # the result doesn't depend on which set is taken as starting point, so the 1st is taken
for i in sets:
    res = res.intersection(i)

# printing the result
if len(res) != 0:
    print(f'intersection of arrays is: {res}')
else:
    print('arrays have no intersection')
