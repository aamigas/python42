"""Реализовать декоратор, который будет приводить все аргументы функции к определенному 
типу данных.

@validation(<type of data (int, float, str, typle, list)>)

после чего будет передавать эти значения в функцию."""


def validation(func):
    def wrapper(arg, type_of_data):
        name = arg
        type_of_argument = type(arg)
        print(f'Переданный аргумент - {name}, тип аргумента - {type_of_argument}')
        arg = type_of_data(arg)
        func(arg, type_of_data)

    return wrapper

@validation
def what_type(arg, type_of_data):
    name = arg
    type_of_argument = type(arg)
    print(f'Приведенный аргумент - {name}, тип аргумента - {type_of_argument}')

what_type('abc', list)
