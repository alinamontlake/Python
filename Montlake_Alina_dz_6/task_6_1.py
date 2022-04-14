"""1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)"""

with open('nginx_logs.txt') as f:
    result = []
    for line in f:
        data = line.split()
        result.append((data[0], data[5].replace('"', ''), data[6]))
        print(result)
