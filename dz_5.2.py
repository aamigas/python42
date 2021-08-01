"""Реализовать генератор, который будет выводить числа фибоначчи."""


def Fibonacci(N):
    F = []
    for i in range(0, N):
        if i <= 1:
            F.append(i)
        else:
            F.append(F[i-1] + F[i-2])
        yield F[i]
        
print(list(Fibonacci(10)))
