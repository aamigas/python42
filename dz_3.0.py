"""Вывести список чисел Фибоначчи (F) от 1 до N"""
N = 6
F = [1, 1]
for i in range(2, N+1):
    F.append(F[i-1] + F[i-2])
print(F)
   

