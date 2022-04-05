"""Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)"""

from random import choice

def get_jokes(n):
    """ Combines nouns + adverbs + adjectives and returns n jokes (sentences)"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    joke = []

    for i in range(0, n):
        joke += [choice(nouns) + " " + choice(adverbs) + " " + choice(adjectives)]
        
    return joke

print(get_jokes(4))
