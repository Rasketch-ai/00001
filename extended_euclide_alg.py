'Для реализации Расширенного Алгоритма Евклида понадобятся обычный алгоритм и список всех пар'
def gcd(n_1, n_2):
    'Алгоритм Евклида'
    r_1 = n_1
    r_2 = n_2
    while r_1 != 0 and r_2 != 0:
        if r_1 > r_2:
            r_1 = r_1 % r_2
        elif r_1 < r_2:
            r_2 = r_2 % r_1
        else:
            break
    if r_1 == 0:
        return r_2
    return r_1
def num_pairs(n_1, n_2):
    'Функция, которая составит список из пар чисел с каждой итерации Алгоритма Евклида'
    numbers = []
    r_1 = n_1
    r_2 = n_2
    while r_1 != 0 and r_2 != 0:
        if r_1 > r_2:
            numbers.append(r_1)
            numbers.append(r_2)
            r_1 = r_1 % r_2
        elif r_1 < r_2:
            numbers.append(r_2)
            numbers.append(r_1)
            r_2 = r_2 % r_1
        else:
            break
    return numbers
def extended_euclide_alg(n_1,n_2):
    'Поиск коофицентов x и y для линейного представления gcd(n_1,n_2)'
    score = 0
    coef_1 = 0
    coef_2 = 1
    while score < (len(num_pairs(n_1,n_2))/2):
        score += 1
        coef_2 = coef_2 - (num_pairs(n_1,n_2)[-2*score]//num_pairs(n_1,n_2)[-2*score+1])*coef_1
        if score == len(num_pairs(n_1,n_2))/2:
            break
        score += 1
        coef_1 = coef_1 - (num_pairs(n_1,n_2)[-2*score]//num_pairs(n_1,n_2)[-2*score+1])*coef_2
    return (coef_1,coef_2)
print(extended_euclide_alg(10983,567)[0],extended_euclide_alg(10983,567)[1])
