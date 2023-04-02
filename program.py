# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

stringEntered = 'a a a b c a a d c d d'
stringSplit = stringEntered.split(' ')
stringResult = ''
dictLetters = {i:0 for i in stringSplit}

for j in range(len(stringSplit)):
    stringResult += f' {stringSplit[j]}'
    if dictLetters[stringSplit[j]] != 0:
        stringResult += f'_{dictLetters[stringSplit[j]]} '
    dictLetters[stringSplit[j]] += 1

stringResult = stringResult[1:-1]
print(stringResult)
