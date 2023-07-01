# Задание 1
# Возьмите 1-3 задачи из тех, что были на прошлых семинарах 
# или в домашних заданиях. Напишите к ним тесты. 2-5 тестов 
# на задачу в трёх вариантах:
#   - doctest,
#   - unittest,
#   - pytest.

import unittest
import pytest


def get_number(number: int, mod: int = 10) -> str:
    """
    Функция получает целое число, систему исчисления и возвращает его  строковое представление.
    :param number: само число
    :param mod: система исчисления
    :return: строковое представление
    >>> get_number(123, 2)
    '1111011'
    >>> get_number(123, 3)
    '11120'
    >>> get_number(123, 4)
    '1323'
    >>> get_number(123, 5)
    '443'
    >>> get_number(123, 6)
    '323'
    >>> get_number(123, 7)
    '234'
    >>> get_number(123, 8)
    '173'
    >>> get_number(123, 9)
    '146'
    """
    result = ''
    while number != 0:
        result = str(number % mod) + result
        number //= mod
    return result


class TestCaseNumbers(unittest.TestCase):
    def test_2(self):
        self.assertEqual(get_number(123, 2), '1111011', msg='Test failed')

    def test_3(self):
        self.assertEqual(get_number(123, 3), '11120', msg='Test failed')

    def test_4(self):
        self.assertEqual(get_number(123, 4), '1323', msg='Test failed')

    def test_5(self):
        self.assertEqual(get_number(123, 5), '443', msg='Test failed')

    def test_6(self):
        self.assertEqual(get_number(123, 6), '323', msg='Test failed')

    def test_7(self):
        self.assertEqual(get_number(123, 7), '234', msg='Test failed')

    def test_8(self):
        self.assertEqual(get_number(123, 8), '173', msg='Test failed')

    def test_9(self):
        self.assertEqual(get_number(123, 9), '146', msg='Test failed')


def test_2():
    assert get_number(123, 2) == '1111011', 'Test failed'


def test_3():
    assert get_number(123, 3) == '11120', 'Test failed'


def test_4():
    assert get_number(123, 4) == '1323', 'Test failed'


def test_5():
    assert get_number(123, 5) == '443', 'Test failed'


def test_6():
    assert get_number(123, 6) == '323', 'Test failed'


def test_7():
    assert get_number(123, 7) == '234', 'Test failed'


def test_8():
    assert get_number(123, 8) == '173', 'Test failed'


def test_9():
    assert get_number(123, 9) == '146', 'Test failed'


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
    unittest.main()
    pytest.main()