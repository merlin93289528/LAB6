vect1 = list(map(float, input('Введіть координати першого ветора через пробіл: ').split(' ')))
vect2 = list(map(float, input('Введіть координати другого ветора через пробіл: ').split(' ')))
summ = 0

if len(vect1) == len(vect2):
    for i in range(len(vect1)):
        summ += vect1[i] * vect2[i]

print(summ)