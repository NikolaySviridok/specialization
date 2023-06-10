# Задание 1
# Напишите функцию, которая получает на вход директорию 
# и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle. 
# - Для дочерних объектов указывайте родительскую директорию. 
# - Для каждого объекта укажите файл это или директория. 
# - Для файлов сохраните его размер в байтах, а для директорий 
#   размер файлов в ней с учётом всех вложенных файлов и 
#   директорий.

import json
import csv
import pickle
import os


def jsn_writer(in_dct: dict, path: str, file_name: str) -> None:
    file_path = os.path.join(path, file_name + '.json')
    with open(file_path, 'w', encoding='utf-8') as f_out:
        json.dump(in_dct, f_out, indent=4)


def csv_writer(in_dct: dict, path: str, file_name: str) -> None:
    file_path = os.path.join(path, file_name + '.csv')
    data = [['Basic_path', 'unit_type',  'unit_name', 'unit_size', ' parent_dir', ]]
    for i_key, i_val in in_dct.items():
        data.append([i_key, *i_val.values()])
    with open(file_path, 'w', encoding='utf-8') as f_out:
        write_csv = csv.writer(f_out, dialect='excel', delimiter=';')
        write_csv.writerows(data)


def pcl_writer(in_dct: dict, path: str, file_name: str) -> None:
    file_path = os.path.join(path, file_name + '.bin')
    with open(file_path, 'wb') as f_out:
        pickle.dump(in_dct, f_out)


def dct_formatter(total_dct: dict[str, dict[str]],
                  path: str,
                  item_name: str,
                  item_type: str) -> None:
    if item_type == 'F':
        total_dct[path] = dict(unit_type='File',
                               unit_name=item_name,
                               unit_size=os.path.getsize(os.path.join(path, item_name)),
                               parent_dir=os.path.split(path)[-1])
    elif item_type == 'D':
        total_dct[path] = dict(unit_type='Directory',
                               unit_name=item_name,
                               unit_size=count_size(os.path.join(path, item_name)),
                               parent_dir=os.path.split(os.path.abspath(path))[-1])


def count_size(count_path: str,
               dir_size: int = 0) -> float:
    for sub_item in os.walk(count_path):
        if sub_item[2]:
            dir_size += sum([os.path.getsize(os.path.join(sub_item[0], file))
                             for file in sub_item[2]])
        if sub_item[1]:
            dir_size += sum([count_size(os.path.join(sub_item[0], subdir))
                             for subdir in sub_item[1]])
    return dir_size


def dir_walker(aim_path: str,
               total_dct: dict = None) -> dict[str, dict[str]]:
    if total_dct is None:
        total_dct = {}
        basic_path = os.path.split(os.path.abspath(aim_path))
        dct_formatter(total_dct,
                      os.path.join(*basic_path[:-1]),
                      basic_path[-1],
                      'D')

    for item in os.listdir(aim_path):
        check_path = os.path.join(aim_path, item)
        if os.path.isfile(check_path):
            dct_formatter(total_dct, aim_path, item, 'F')
        elif os.path.isdir(check_path):
            dct_formatter(total_dct, aim_path, item, 'D')
            dir_walker(os.path.join(aim_path, item), total_dct)
    return total_dct


def dict_printer(in_dict: dict) -> None:
    for i_key, i_val in sorted(in_dict.items()):
        print(i_key, end=':')
        if isinstance(i_val, dict):
            print()
            dict_printer(i_val)
        else:
            print('\t', i_val)


def main():
    tst_path = '/home/andrew/Documents/geekbrains/Python2023/Homeworks/'
    result = dir_walker(tst_path)
    jsn_writer(result, os.getcwd(), 'result')
    pcl_writer(result, os.getcwd(), 'result')
    csv_writer(result, os.getcwd(), 'result')


if __name__ == '__main__':
    main()