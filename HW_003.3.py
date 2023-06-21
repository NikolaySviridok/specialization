# Задание 3
# Создайте словарь со списком вещей для похода в качестве ключа 
# и их массой в качестве значения. Определите какие вещи влезут 
# в рюкзак передав его максимальную грузоподъёмность. Достаточно 
# вернуть один допустимый вариант. *Верните все возможные 
# варианты комплектации рюкзака.

def backpack(shop: dict[str:int], size: int) -> list[list[str]]:
    pcs, weight = zip(*sorted(shop.items(), key=lambda x: x[1], reverse=True))
    result, temp, temp_w = [], [], 0
    for index, w in enumerate(weight, 0):
        temp_w += w
        temp.append((pcs[index]))
        for index_n, wn in enumerate(weight[index:], index):
            if wn + temp_w <= size:
                temp_w += wn
                temp.append(pcs[index_n])
        result.append(temp)
        temp, temp_w = [], 0
    return result