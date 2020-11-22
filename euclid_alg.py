''' Вычисление Н.О.Д. чисел, вводимых пользователем'''
print("Введите два натуральных числа, отличных от 1")
number_1 = int(input())
number_2 = int(input())
def gcd(n_1, n_2):
    ''' Алгоритм Евклида '''
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
print(gcd(number_1, number_2))
