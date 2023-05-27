# Задание 2
# Напишите программу, которая принимает две строки вида “a/b” 
# - дробь с числителем и знаменателем. Программа должна возвращать
# сумму и произведение* дробей. Для проверки своего кода 
# используйте модуль fractions.

class UserFractions:
    def __init__(self, top: int, bottom: int, integer=0):
        self.top = top
        self.bottom = bottom
        self.__integer = integer

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, top: int):
        self._top = top

    @property
    def bottom(self):
        return self._bottom

    @bottom.setter
    def bottom(self, bottom: int):
        self._bottom = bottom

    @property
    def integer(self):
        self.__integer += self.top // self.bottom
        self.top %= self.bottom
        return self.__integer

    @staticmethod
    def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

    def __str__(self):
        if self.integer:
            return f'{self.integer} {self.top}/{self.bottom}' if self.top != 0 else str(self.integer)
        else:
            return f"{self.top}/{self.bottom}"

    def __add__(self, other):
        if isinstance(other, int):
            temp = self.top + (other + self.integer) * self.bottom
            return UserFractions(temp, self.bottom)
        if isinstance(other, UserFractions):
            temp_top = self.top * other.bottom + self.bottom * other.top
            temp_bottom = self.bottom * other.bottom
            temp_gcd = UserFractions.gcd(temp_top, temp_bottom)
            return UserFractions(temp_top // temp_gcd, temp_bottom // temp_gcd, self.integer + other.integer)
        print(f'Дробное число нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            temp = self.integer * other * self.bottom + self.top * other
            return UserFractions(temp, self.bottom)
        if isinstance(other, UserFractions):
            temp_top_self = self.bottom * self.integer + self.top
            temp_top_other = other.bottom * other.integer + other.top
            return UserFractions(temp_top_self * temp_top_other, self.bottom * other.bottom)
        print(f'Дробное число нельзя умножить на {other}')