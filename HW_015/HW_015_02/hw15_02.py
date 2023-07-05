# Возьмите любые 1-3 задачи из прошлых домашних заданий.
#  - Добавьте к ним логирование ошибок и полезной информации.
#  - Также реализуйте возможность запуска из командной строки
#    с передачей параметров.

import argparse
from last_works import ATM, FileListerWorks


def atm_task() -> None:
    atm = ATM()
    atm.work()


def file_search(start_path: str, file_ext: str) -> None:
    dir_walker = FileListerWorks(start_path)
    for item in dir_walker.list_dir(file_ext):
        print(item)


def main():
    parser = argparse.ArgumentParser(description='hw15_task02')
    parser.add_argument('m', metavar='mode', help='Mode switch: "atm" for ATM, "files" for file recursive search')
    parser.add_argument('-p', metavar='path', type=str,
                        help='Path to search files (default: current dir)', default='.')
    parser.add_argument('-e', metavar='ext', type=str,
                        help='Files extension to search (without dot, default \'py\')', default='py')
    args = parser.parse_args()
    if args.m == 'atm':
        atm_task()
    elif args.m == 'files':
        file_search(args.p, args.e)


if __name__ == '__main__':
    main()