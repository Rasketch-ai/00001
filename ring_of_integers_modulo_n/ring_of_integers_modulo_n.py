import euclid_jokes
import numbers
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
        if euclid_jokes.gcd(self.value, self.divider) == 1: # Равенство НОДа элемента и модуля единице говорит об обратимости элемента.
            return True
        else:
            return False

    def __reverse_element__(self): # Находим элемент, обратный к данному.
        if self.__reversibility__() == True:
            if (self.value * (euclid_jokes.extended_euclide_alg(self.value, self.divider)[0] % self.divider)) % self.divider == 1:
                return Integers_Modulo_N(euclid_jokes.extended_euclide_alg(self.value, self.divider)[0] % self.divider, self.divider)
            else:
                return Integers_Modulo_N(euclid_jokes.extended_euclide_alg(self.value, self.divider)[1] % self.divider, self.divider)

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
