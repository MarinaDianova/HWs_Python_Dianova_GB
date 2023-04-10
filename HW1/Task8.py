# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите ширину шоколадки n: '))
m = int(input('Введите длину шоколадки n: '))
k = int(input('Введите количество долек k: '))

if k < n * m and (k % n == 0 or k % m == 0):
    print('От шоколадки размером', n, 'х', m, 'МОЖНО отломить кусок размером', k, 'долек')
else:
    print('От шоколадки размером', n, 'х', m, 'НЕЛЬЗЯ отломить кусок размером', k, 'долек')