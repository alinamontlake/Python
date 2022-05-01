"""1.Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы."""

# Создаём класс:
class Matrix:
    info = "Матрица"
# Создаём атрибут:
    def __init__(self, list1, list2, list3):
        self.list1 = list1
        self.list2 = list2
        self.list3 = list3
        self.matrix = [list1, list2, list3]
# Создаём методы:
    def __str__(self):
        super().__init__()
        print(f"Матрица #1: {self.matrix}")
    def __add__(self, other):
        return f" Сумма #1: {[(self.list1[0] + x1.list1[0],self.list1[1] + x1.list1[1]), (self.list2[0] + x1.list2[0],self.list2[1] + x1.list2[1]), (self.list3[0] + x1.list3[0],self.list3[1] + x1.list3[1])]}"
# Создаём класс:
class Matrix2(Matrix):
# Создаём атрибут:
    def daat (self, matrix, list1, list2, list3):
        Matrix.__init__(matrix, list1, list2, list3)
# Создаём методы:
    def __str__(self):
        print(f"Матрица #2: {self.matrix}")
    def __add__(self, other):
        return f" Сумма #2 : {[(self.list1[0] + other.list1[0],self.list1[1] + other.list1[1]), (self.list2[0] + other.list2[0],self.list2[1] + other.list2[1]), (self.list3[0] + other.list3[0],self.list3[1] + other.list3[1])]}"
x = Matrix((1, 12), (7, 11), (3, 12))
x2 = Matrix2((1, 130), (0, 44), (32, 23))
x1 = Matrix2((7, 670), (5, 11), (3, 12))
x.__str__()
x1.__str__()
print(x + x1)
print(x1 + x2)
