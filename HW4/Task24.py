# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть 
# ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

import random

n = int(input('Введите количество кустов N: '))
berries = [random.randint(0, 100) for i in range(n)]
print(f'Урожай с каждого куста: {berries}')

sum = []

# Долгий вариант:
# for i in range(len(berries)-1):
#     if i == 0:
#         sum.append(berries[-1] + berries[0] + berries[1])
#     elif i == n:
#         sum.append(berries[-2] + berries[-1] + berries[0])
#     else:
#         sum.append(berries[i-1] + berries[i] + berries[i+1])

# Правильный вариант:
for i in range(len(berries)-1):
    sum.append(berries[i-1] + berries[i] + berries[i+1])
else:
    sum.append(berries[-2] + berries[-1] + berries[0])
    

print(sum)
print(f'Максимальное количество ягод, которое можно собрать за 1 заход: {max(sum)}')
