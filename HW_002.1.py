# Задание 1
# Напишите программу, которая получает целое число и возвращает 
# его шестнадцатеричное строковое представление. Функцию hex 
# используйте для проверки своего результата.

def hex_number(number: int, mod: int = 16) -> str:
    result = ''
    while number != 0:
        temp = number % mod if (number % mod) < 10 else chr(number % mod + 87)
        result = str(temp) + result
        number //= mod
    result = "0x" + result
    return result