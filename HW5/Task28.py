# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2 -> 4

def summa(a, b):
    if b > 0:
        a = a + 1
        return summa(a, b - 1)
    return a


A = int(input('Введите целое положительное число A: '))
B = int(input('Введите целое положительное число B: '))
print(f'{A} + {B} = {summa(A, B)}')