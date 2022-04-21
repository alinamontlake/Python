"""2.(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания."""

result = {}
with open('nginx_logs.txt') as f:
    for line in f:
        remote_add = line[:line.find(' ')]
        result.setdefault(remote_add, 0)
        result[remote_add] += 1

result = sorted(result.items(), key=lambda items: items[1], reverse=True)
print(f'IP адрес спамера = {result[0][0]}, количество запросов = {result[0][1]}')
