"""4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. """

def thesaurus(*firstname):
    names_dictionary = {}
    for name in firstname:
        if name[0] in names_dictionary:
            names_dictionary[name[0].append(name)]
        else:
            names_dictionary[name[0]]=[name]
    print(sorted(names_dictionary.items()))

    
thesaurus('Владислав', 'Алина', 'Маргарита', 'Есения')



def thesaurus_adv(*full_name_list):
    name = dict()
    for item in full_name_list:
        name.setdefault(item.split()[1][:1], []).append(item)

    for key, full_name in name.items():
        name[key] = thesaurus(*full_name)

    return name

print(thesaurus_adv("Алина Монтлейк", "Александр Артемьев", "Григорий Остапов", "Валерий Меладзе"))
