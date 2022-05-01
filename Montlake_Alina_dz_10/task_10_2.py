"""2.Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property."""

#Создаём класс:
class Clothes:
    info = "<<Программа для подсчёта расхода ткани на одежду>>"
    # Создаём атрибут:
    def __init__(self, size=52, height=184):
        self.size = size
        self.height = height
# Создаём дочерний класс:
class Suit(Clothes):
    def sd(self, height):
        self.height = height
        return (2 * height + 0.3)
class Coat(Clothes):
    def cd(self, size):
        self.size = size
        return (size / 6.5) + 0.5
class Time:
    def __init__(self, days = 5):
        self.days = days
# Создаём свойство
    @property
    def days(self):
        return self.days * 8
# Создаём сеттер
    @days.setter
    def days (self, days):
        if days < 1:
            self.days = "малый расход"
        elif days < 9:
            self.days = "средний расход"
        else:
            self.days = "максимальный расход"
    def info(self):
        print(f"{x3.days} часов- {str(self.days)}")
x = Clothes()
x1 = Suit(x.height)
x2 = Coat(x.size)
x3 = Time()
print(x.info)
print(x1.sd(x.height))
print(round(x2.cd(x.height)))
