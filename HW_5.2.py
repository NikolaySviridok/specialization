# Создайте функцию генератор чисел Фибоначчи.

def fibona44i(limit: int):
    fibo = [0, 1]
    while limit > 0:
        yield fibo[-1]
        fibo.append(fibo[-1] + fibo[-2])
        limit -= 1
for number in fibona44i(10):
    print(number)