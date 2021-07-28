"""Реализовать функцию, которая будет выводить снежинку в файл. 
На вход дается число N, которое будет показывать длину ребра снежинки.
N=2    **
       ***
       ** """


def snowflake(N):
    f = open('snow.txt', 'w')
    s = [(N - i -1) * ' ' + (i + N) * '* ' for i in range(N)]
    s = s + s[N-2::-1]
    for i in s:
        f.write(i + '\n')
    f.close()

snowflake(int(input('Введите размер ребра снежинки ', ))) 