# HWs_Python_Dianova_GB

# Задачи Семинара 1:
## Задача 2: 

Найдите сумму цифр трехзначного числа. 

**Образец:**

*123 -> 6 (1 + 2 + 3)*

*100 -> 1 (1 + 0 + 0)*

## Задача 4: 
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

**Образец:**

*6 -> 1 4 1*

*24 -> 4 16 4*

*60 -> 10 40 10*

## Задача 6: 
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

**Образец:**

*385916 -> yes*
*123456 -> no*

## Задача 8:
Требуется определить, можно ли от шоколадки размером n # × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

**Образец:**

*3 2 4 -> yes*

*3 2 1 -> no*


# Задачи Семинара 2:
## Задача 10:
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное количество монет, оторые нужно перевернуть.

**Образец:**

*5 -> 1 0 1 1 0*

*2*

## Задача 12: 
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

**Образец:**

*4 4 -> 2 2*

*5 6 -> 2 3*

## Задача 14: 
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

**Образец:**

*10 -> 1 2 4 8*

# Задачи Семинара 3:
## Задача 16: 
Требуется вычислить, сколько раз встречается некоторое число X в массиве A. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X.

**Образец:**

*5*

*7 -2 3 5 1*

*3 -> 1*

## Задача 18: 
Требуется найти в массиве A самый близкий по величине элемент к заданному числу X. Если таких элементов несколько, вывести один любой. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X

**Образец:**

*5*

*7 -2 3 5 1*

*6 -> 7*

## Задача 20:
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так: 
- A, E, I, O, U, L, N, S, T, R – 1 очко; 
- D, G – 2 очка; B, C, M, P – 3 очка; 
- F, H, V, W, Y – 4 очка; K – 5 очков; 
- J, X – 8 очков; 
- Q, Z – 10 очков. 

А русские буквы оцениваются так: 
- А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
- Д, К, Л, М, П, У – 2 очка; 
- Б, Г, Ё, Ь, Я – 3 очка; 
- Й, Ы – 4 очка; 
- Ж, З, Х, Ц, Ч – 5 очков; 
- Ш, Э, Ю – 8 очков; 
- Ф, Щ, Ъ – 10 очков. 

Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

**Образец:**

*ноутбук -> 12*
