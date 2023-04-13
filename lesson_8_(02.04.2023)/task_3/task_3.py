"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

data = {
    'items':
        ['copybook', 'pencil', 'rubber', 'line'],
    'items_quantity': 4,
    'items_price':
        {'copybook': '5€', 'pencil': '2€', 'rubber': '1€', 'line': '4€'}
}

with open('my_file.yaml', 'w', encoding='utf-8') as file:
    content = yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

with open('my_file.yaml', encoding='utf-8') as file:
    content = yaml.load(file, Loader=yaml.FullLoader)
    print(content)
