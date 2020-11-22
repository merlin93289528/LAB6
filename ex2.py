from math import factorial

n = int(input("Введіть кількість елементів: "))
mass = []
chs = 0
summ = 0

for i in range(1, n + 1):
    chs = chs + ((-1)**i)*i
    mass.append(chs / factorial(i))
    if mass[-1] > 0:
        summ += mass[-1]

print(mass)
print(summ)