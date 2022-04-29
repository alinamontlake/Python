"""3.Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

>>> a = calc_cube(5)
5: <class 'int'> """

from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper_logger(arg):
        print(f'{calc_kube.__name__}({arg}: {type(arg)})')
        return func(arg)
    return wrapper_logger


@type_logger
def calc_kube(answer):
    return answer ** 3


a = calc_kube(5)
print(a)
