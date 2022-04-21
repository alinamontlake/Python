"""1.Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError."""

import re

RE_NAME = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_.+-]+\@[a-zA-Z0-9-]+\.[a-zA-Z]+$')


def email_parse(email_address):
    assert RE_NAME.match(email_address), f'ValueError: wrong email: {email_address}'
    my_dict = {}
    my_dict.update({'username': email_address.split('@')[0]})
    my_dict.update({'domain': email_address.split('@')[1]})
    return my_dict


print(email_parse('ivan.ivanov@mail.ru'))
print(email_parse('123ivan-ivanov@mail.ru'))
print(email_parse('ivan.ivanov@mailru'))
