# Задание 2
# Напишите функцию принимающую на вход только ключевые 
# параметры и возвращающую словарь, где ключ — значение 
# переданного аргумента, а значение — имя аргумента. Если 
# ключ не хешируем, используйте его строковое представление.

def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result


print(kwargs_to_dict(name='Андрей', age=45,
                     has_work=True, commands=['ККН', 'LM', 'DP'],
                     growth=1.87, nicks={'STONE', '17th'}))