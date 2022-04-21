"""3.Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?"""


def thesaurus(*firstname):
    names_dictionary = {}
    for name in firstname:
        if name[0] in names_dictionary:
            names_dictionary[name[0].append(name)]
        else:
            names_dictionary[name[0]]=[name]
    print(sorted(names_dictionary.items()))

    
thesaurus('Владислав', 'Алина', 'Маргарита', 'Есения')
            
    
