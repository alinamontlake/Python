"""2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. """

eng_to_rus_numbers = {
    'zero' :'ноль',
    'one' : 'один',
    'two' : 'два',
    'three' : 'три',
    'four' : 'четыре',
    'five' : 'пять',
    'six' : 'шесть',
    'seven' : 'семь',
    'eight' : 'восемь',
    'nine' : 'девять',
    'ten' : 'десять'
    }

def num_translate_adv(en_numbers):
    if en_numbers == en_numbers.lower():
        return eng_to_rus_numbers.get(en_numbers.lower())
    elif en_numbers == en_numbers.capitalize():
        return eng_to_rus_numbers.get(en_numbers.lower()).capitalize()
    elif en_numbers is None:
        return None
print (num_translate_adv('Nine'))
print (num_translate_adv('eleven'))
print (num_translate_adv('two'))


