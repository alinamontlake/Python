"""2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt"""

import re
REMOTE_ADDR = re.compile(r'\d+\.\d+\.\d+\.\d+')
REQUEST_DATETIME = re.compile(r'\d+/\w+/\d+:\d+:\d+:\d+\s[+]\d+')
REQUEST_TYPE = re.compile(r'[A-Z]{3}')
REQUESTED_RESOURSE = re.compile(r'[/][a-z]+[/][a-z]+[_][0-9]+')
RESPONSE_CODE_SIZE = re.compile(r'\s\d{1,3}')
# Хватило ума только на то, что бы объединить CODE и SIZE

with open('nginx_logs.txt', encoding='utf-8') as log_file:
    for line in log_file.readlines():
        parsed_raw = (re.search(REMOTE_ADDR, line).group(0), re.search(REQUEST_DATETIME, line).group(0),
                      re.search(REQUEST_TYPE, line).group(0), re.search(REQUESTED_RESOURSE, line).group(0),
                      tuple(re.findall(RESPONSE_CODE_SIZE, line)))
        print(parsed_raw)
