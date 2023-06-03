# Задание 1
# В модуль с проверкой даты добавьте возможность запуска 
# в терминале с передачей даты на проверку.

from datetime import datetime
from sys import argv


def date_validate(date_text: str) -> bool:
    try:
        value = datetime.strptime(date_text, "%d.%m.%Y").date()
        return True
    except:
        return False


def _leap_info(date_text: str) -> bool:
    year = int(date_text.split(".")[-1])
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    date_validate(argv[2])