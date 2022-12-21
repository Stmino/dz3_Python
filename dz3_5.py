# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:  - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('Введите длину ряда: '))
f0=0
f1 = f2 = 1
fib=[]
fib.append(f0)
fib.append(f1)
fib.append(f2)
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    fib.append(f2)
nefib=fib[1:]
nefib.reverse()
for i in range(len(nefib)):
    while i < len(nefib):
            nefib[i]=-nefib[i]
            i=i+1
newfib=nefib+fib
print(newfib)
