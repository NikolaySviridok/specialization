# Задание 2
# Соберите из созданных на уроке и в рамках домашнего 
# задания функций пакет для работы с файлами.

from pathlib import Path
from typing import TextIO


__all__ = ['from_two_files']


def _read_or_begin(fd: TextIO) -> str:
    line = fd.readline()
    if line == '':
        fd.seek(0)
        return _read_or_begin(fd)
    return line[:-1]


def from_two_files(numbers: Path, strings: Path, result: Path) -> None:
    with (
        open(numbers, 'r', encoding='utf-8') as f_num,
        open(strings, 'r', encoding='utf8') as f_str,
        open(result, 'w', encoding='utf-8') as f_res
    ):
        len_str = sum(1 for _ in f_str)
        len_num = sum(1 for _ in f_num)
        for _ in range(max(len_str, len_num)):
            name = _read_or_begin(f_str)
            two_num = _read_or_begin(f_num)
            num_i, num_f = two_num.split('|')
            mult = int(num_i) * float(num_f)
            if mult < 0:
                f_res.write(f'{name.lower()} {-mult}\n')
            elif mult > 0:
                f_res.write(f'{name.upper()} {int(-mult)}\n')