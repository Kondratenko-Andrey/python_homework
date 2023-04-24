"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

command_domain = ['ping', 'yandex.ru']
domain_ping = subprocess.Popen(command_domain, stdout=subprocess.PIPE)

for line in domain_ping.stdout:
    res = chardet.detect(line)
    print(line.decode(encoding=res['encoding']))

command_domain = ['ping', 'youtube.com']
domain_ping = subprocess.Popen(command_domain, stdout=subprocess.PIPE)

for line in domain_ping.stdout:
    res = chardet.detect(line)
    print(line.decode(encoding=res['encoding']))
