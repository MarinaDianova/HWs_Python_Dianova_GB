# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X.

# *Пример:*
# 5
# 7 -2 3 5 1
# 3
# -> 1

import random
n = int(input('Введите количество элементов массива: '))
lst = [random.randint(-10, 10) for i in range(n)]
print(lst)

x = int(input('Введите искомое число: '))

cnt = 0
for el in lst:
    if x == el:
        cnt += 1

print(f'Число {x} встречается {cnt} раз')
