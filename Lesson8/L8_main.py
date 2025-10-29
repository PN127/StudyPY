n = int(input('Введите число'))

def fib(n):
    x = 0
    y = 1
    while x<n:
        yield x
        x, y = y, x+y

for i in fib(n):
    print(i)