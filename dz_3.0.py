"""Вывести список чисел Фибоначчи (F) от 1 до N с помощью цикла"""
N = int(input('Введите число ', ))

s = 0
F = []
for i in range(N):
    if i <= 1:
        F.append(i)
    else:
        F.append(F[i-1] + F[i-2])
        s += 1
print(F)
print('Количество вызовов операции сложения без рекурсии равно ', s)
   
"""Вывести список чисел Фибоначчи (F) от 1 до N через рекурсию"""

def fibon(n):
  if n <= 1:
      return n    
  else:
      global m; m += 1
      return (fibon(n-1) + fibon(n-2)) 

F = []
m = 0
for i in range(int(N)):
    F.append(fibon(i))
print(F)
print('Количество вызовов операции сложения с рекурсией равно ', m)


