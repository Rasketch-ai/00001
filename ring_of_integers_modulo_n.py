import numbers
''' Функции, которые пригодятся '''
def gcd(n_1, n_2):# Алгоритм Евклида
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
def num_pairs(n_1, n_2):# Вспомогательная фунцкия для расширенного Алгоритма Евклида
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
def extended_euclide_alg(n_1,n_2): # Расширенный Алгоритм Евклида
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
    return (coef_2,coef_1)

N = 7
class Integers_Modulo_N:
    def __init__(self, value):
        if isinstance(value,numbers.Integral):
            self.value = value % N
        else: 
            raise TypeError

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __add__(self, other):
        summ = (self.value + other.value) % N
        return Integers_Modulo_N(summ)

    def __neg__(self):
        opposite = -1 * self.value
        return Integers_Modulo_N(opposite)

    def __mul__(self, other):
        multiplication = (self.value * other.value) % N
        return Integers_Modulo_N(multiplication)

    def __reversibility__(self): # Проверяем обратимость элемента.
        if gcd(self.value, N) == 1: # Равенство НОДа элемента и модуля единице говорит об обратимости элемента.
            return True
        else:
            return False

    def __reverse_element__(self): # Находим элемент, обратный к данному.
        if self.__reversibility__() == True:
            if (self.value * (extended_euclide_alg(self.value, N)[0] % N)) % N == 1:
                return Integers_Modulo_N(extended_euclide_alg(self.value, N)[0] % N)
            else:
                return Integers_Modulo_N(extended_euclide_alg(self.value, N)[1] % N)

    def __truediv__(self, other):
        if other.__reversibility__() == False:
            print("Нельзя делить на необратимый элемент")
            raise ValueError
        else:
            division_value = self.value * other.__reverse_element__().value
        return Integers_Modulo_N(division_value)
a = Integers_Modulo_N(0)
b = Integers_Modulo_N(1)
c = Integers_Modulo_N(2)
d = Integers_Modulo_N(3)
e = Integers_Modulo_N(4)
f = Integers_Modulo_N(5)
g = Integers_Modulo_N(6)
h = Integers_Modulo_N(8)
print(a)
print(d + g)
print(a + (-b))
print(b == h)
print(c * e)
print(a.__reversibility__())
print(f.__reverse_element__())
print(f / e)