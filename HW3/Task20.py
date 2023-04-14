# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*
# ноутбук -> 12

word = input('Введите слово: ').upper()

dict = {1:"AEIOULNSTRАВЕИНОРСТ", 2:"DGДКЛМПУ", 3:"BCMPБГЁЬЯ", 4:"FHVWYЙЫ", 5:"KЖЗХЦЧ", 8:"JXШЭЮ", 10:"QZФЩЪ"}

sum = 0

for i in word:
    for key, val in dict.items():
        if i in val:
            sum += key
        
print(f'Стоимость слова {word}: {sum}')




# # Задаем словарь объединением
# letters1 = ('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R')
# val1 = '1'
# dict1 = dict.fromkeys(val1, letters1)

# letters2 = ('Д', 'К', 'Л', 'М', 'П', 'У', 'D', 'G')
# val2 = '2'
# dict2 = dict.fromkeys(val2, letters2)

# letters3 = ('Б', 'Г', 'Ё', 'Ь', 'Я', 'B', 'C', 'M', 'P')
# val3 = '3'
# dict3 = dict.fromkeys(val3, letters3)

# letters4 = ('Й', 'Ы', 'F', 'H', 'V', 'W', 'Y')
# val4 = '4'
# dict4 = dict.fromkeys(val4, letters4)

# letters5 = ('Ж', 'З', 'Х', 'Ц', 'Ч', 'K')
# val5 = '5'
# dict5 = dict.fromkeys(val5, letters5)

# letters6 = ('Ш', 'Э', 'Ю', 'J', 'X')
# val6 = '8'
# dict6 = dict.fromkeys(val6, letters6)

# letters7 = ('Ф', 'Щ', 'Ъ', 'Q', 'Z')
# val7 = '10'
# dict7 = dict.fromkeys(val7, letters7)

# dict = dict2 | dict1 | dict3 | dict4 | dict5 | dict6 | dict7

# print(dict)