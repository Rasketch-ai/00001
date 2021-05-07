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








class Integers_Modulo_N:
    def __init__(self, value, divider):
        if isinstance(value,numbers.Integral):
            self.divider = divider
            self.value = value % divider
        else: 
            raise TypeError

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if other.divider != self.divider:
            raise TypeError
        else:
            qwerty = bool(self.value == other.value)
        return qwerty

    def __add__(self, other):
        if other.divider != self.divider:
            raise TypeError
        else:
            summ = (self.value + other.value) % self.divider
        return Integers_Modulo_N(summ, self.divider)

    def __neg__(self):
        opposite = -1 * self.value
        return Integers_Modulo_N(opposite, self.divider)

    def __mul__(self, other):
        if other.divider != self.divider:
            raise TypeError
        else:
            multiplication = (self.value * other.value) % self.divider
        return Integers_Modulo_N(multiplication, self.divider)

    def __reversibility__(self): # Проверяем обратимость элемента.
        if gcd(self.value, self.divider) == 1: # Равенство НОДа элемента и модуля единице говорит об обратимости элемента.
            return True
        else:
            return False

    def __reverse_element__(self): # Находим элемент, обратный к данному.
        if self.__reversibility__() == True:
            if (self.value * (extended_euclide_alg(self.value, self.divider)[0] % self.divider)) % self.divider == 1:
                return Integers_Modulo_N(extended_euclide_alg(self.value, self.divider)[0] % self.divider, self.divider)
            else:
                return Integers_Modulo_N(extended_euclide_alg(self.value, self.divider)[1] % self.divider, self.divider)

    def __truediv__(self, other):
        if other.divider != self.divider:
            raise TypeError
        else:
            if other.__reversibility__() == False:
                print("Нельзя делить на необратимый элемент")
                raise ValueError
            else:
                division_value = self.value * other.__reverse_element__().value
            return Integers_Modulo_N(division_value, self.divider)

