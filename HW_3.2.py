# Задание 2
# В большой текстовой строке подсчитать количество встречаемых 
# слов и вернуть 10 самых частых. Не учитывать знаки препинания 
# и регистр символов. За основу возьмите любую статью из 
# википедии или из документации к языку.

def ten_popular(text: str) -> list[str]:
    delete = ".,!?;:-[]{}()="
    for i in delete:
        text = text.replace(i, "")
    text = text.lower()
    return sorted(set(text.split()), key=lambda x: text.count(x))[-10:]
