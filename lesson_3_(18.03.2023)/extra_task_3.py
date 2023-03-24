"""
ДОПОЛНИТЕЛЬНЫЕ ЗАДАНИЯ:
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D,
G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
либо только русские буквы.

*Пример:*

ноутбук
    12
"""


def english_words(eng_word):
    points = 0
    one_point = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
    two_points = ['D', 'G']
    three_points = ['B', 'C', 'M', 'P']
    four_points = ['F', 'H', 'V', 'W', 'Y']
    five_points = ['K']
    eight_points = ['J', 'X']
    ten_points = ['Q', 'Z']
    for i in range(len(eng_word)):
        if one_point.count(eng_word[i].upper()) > 0:
            points += 1
        elif two_points.count(eng_word[i].upper()) > 0:
            points += 2
        elif three_points.count(eng_word[i].upper()) > 0:
            points += 3
        elif four_points.count(eng_word[i].upper()) > 0:
            points += 4
        elif five_points.count(eng_word[i].upper()) > 0:
            points += 5
        elif eight_points.count(eng_word[i].upper()) > 0:
            points += 8
        elif ten_points.count(eng_word[i].upper()) > 0:
            points += 10
    return points


def russian_words(rus_word):
    points = 0
    one_point = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
    two_points = ['Д', 'К', 'Л', 'М', 'П', 'У']
    three_points = ['Б', 'Г', 'Ё', 'Ь', 'Я']
    four_points = ['Й', 'Ы']
    five_points = ['Ж', 'З', 'Х', 'Ц', 'Ч']
    eight_points = ['Ш', 'Э', 'Ю']
    ten_points = ['Ф', 'Щ', 'Ъ']
    for i in range(len(rus_word)):
        if one_point.count(rus_word[i].upper()) > 0:
            points += 1
        elif two_points.count(rus_word[i].upper()) > 0:
            points += 2
        elif three_points.count(rus_word[i].upper()) > 0:
            points += 3
        elif four_points.count(rus_word[i].upper()) > 0:
            points += 4
        elif five_points.count(rus_word[i].upper()) > 0:
            points += 5
        elif eight_points.count(rus_word[i].upper()) > 0:
            points += 8
        elif ten_points.count(rus_word[i].upper()) > 0:
            points += 10
    return points


word = input('Введите слово: ')

if english_words(word) > 0:
    print(f'Вы ввели слово английским алфавитом и оно набрало {english_words(word)} очков!')
elif russian_words(word):
    print(f'Вы ввели слово русским алфавитом и оно набрало {russian_words(word)} очков!')
