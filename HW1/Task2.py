# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = int(input('Введите трёхзначное число: '))
if a < 1000 and a > 99:

    print('Cумма цифр числа', a, ' = ', a % 10 + a // 10 % 10 + a // 100)
else:
    print('Вы ввели не трёхзначное число')