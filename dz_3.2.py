"""Задача 2
Написать программу, где:
Ввод:
Первый аргумент который сохраняется в одну переменную.(input, от 3 до 23)
Второй аргумент который сохраняется в другую переменную.(input, от 3 до 23)
Третий аргумент который является операцией(+, -, *, /)
Вывод:
Данная операция должна произойти с использованием первых двух аргументов."""
import sys
a = input('введите значение от 3 до 23  ' , )
b = input('введите значение от 3 до 23  ' , )
op = input ('введите тип операции (+, -, *, /):  ' , )
try:
    float(a + b)
except: 
    ValueError
    print(' values are out of range')
    sys.exit()
if (3 <= float(a) <= 23) and (3 <= float(b) <= 23) and op in ('+-*/'):
    print(eval(a + op + b))
else:
    print(' values are out of range')
