# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе
# несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает
# в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

# Ввод: пара-ра-рам рам-пам-папам
# Вывод: па-ра-па-дам Парам пам-пам

# Вариант 1: С циклами

# #Считаем гласные в каждом слове
# def count_vowels(string):
#     vowels = 'ауоыэяюёие'
#     count_syllable = []

#     for i in string:
#         count = 0
#         for letter in i:
#             if letter in vowels:
#                 count += 1
#         count_syllable.append(count)
#     return count_syllable

# # Проверяем ритм
# def rithm(count_array):
#     if len(set(count_array)) == 1:
#         return print('Парам пам-пам')
#     else:
#         return print('Пам парам')


# poem = input('Введите стихотворение: ')
# # # poem = 'пара-ра-рам рам-пам-папам'
# # rithm(count_vowels(poem.lower().split()))

# # Вариант 2:

# def rithm(string):
#     action = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
#     tmp = action(string[0])
#     if all(action(i) == tmp for i in string):
#         return 'Парам пам-пам'
#     return 'Пам парам'

# # poem = 'пара-ра-рам рам-пам-папам'
# poem = input('Введите стихотворение: ')
# print(rithm(poem.lower().split()))


# Вариант 3: С функцией высшего порядка

vowels = 'ауоыэяюёие'


def rithm(operation, poem):
    count_vowels = []
    for word in poem:
        count_vowels.append(operation(word))
    if len(set(count_vowels)) == 1:
        return print('Парам пам-пам')
    else:
        return print('Пам парам')


poem = input('Введите стихотворение: ')
# poem = 'пара-ра-рам рам-пам-папам'
rithm(lambda x: sum(1 for i in x if i in vowels), poem.lower().split())
