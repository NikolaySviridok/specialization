# задание 3
# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать 
# “больше” или “меньше” после каждой попытки.

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

def search():
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    search_num = -1
    count = 10
    while search_num != num:
       search_num = int(input("Угадайте число: "))
    print([["Загаданное число меньше", "Загаданное число больше"][search_num < num], "Угадали!"][search_num == num])
    count -= 1
    print("Попытки закончились") if count == 0: break