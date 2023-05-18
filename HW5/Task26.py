# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    return power(a, b - 1) * a

# Вариант 2: Рекурсия в лямбда функции
# power = lambda a, b: a * power(a, b - 1) if b else 1

A = int(input('Введите целое положительное число A: '))
B = int(input('Введите целое положительное число B: '))
print(f'Число {A} в степени {B} равно {power(A, B)}')