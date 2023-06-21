# Задание 1
# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При 
#   переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. 
#   Переименование должно работать только для этих файлов 
#   внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. 
#   Например для диапазона [3, 6] берутся буквы с 3 по 6 из 
#   исходного имени файла. К ним прибавляется желаемое конечное 
#   имя, если оно передано. Далее счётчик файлов и расширение.

import os


def rename_files(dir_path: str,
                 new_name: str = '',
                 count: int = 3,
                 in_extension: str = 'txt',
                 out_extension: str = 'txt',
                 slice_name: tuple = (0, 0)):
    if not os.path.isdir(dir_path):
        return False
    file_list = os.listdir(dir_path)
    files_count = 1
    for cur_file in file_list:
        cur_name, cur_ext = cur_file.split('.')
        if cur_ext == in_extension:
            new_file = ''
            if slice_name:
                new_file += f'{cur_name[slice_name[0]:slice_name[1]]}'
            if new_name:
                new_file += f'{new_name}'
            new_file += f'_{files_count:0>{count}}.{out_extension}'
            os.rename(os.path.join(dir_path, cur_file),
                      os.path.join(dir_path, new_file))
            files_count += 1
    return f'{files_count} файл(а/ов) переименован(ы) по шаблону ' \
           f'"old_name[{slice_name[0]}:{slice_name[1]}]{new_name}_{"X" * int(f"{count}")}.{out_extension}"'


print(rename_files('Example_files', new_name='NewSuper', count=5, in_extension='txt',
                   out_extension='doc', slice_name=(5, 30)))
