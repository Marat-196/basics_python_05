# 4. Создайте функцию генератор чисел Фибоначчи
# https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

def fibonacci(n: int):
    if n == 0:
        yield 0
    elif n == 1:
        yield 1
    else:
        f1, f2 = 0, 1
        for _ in range(n):
            yield f1
            f1, f2 = f2, f1 + f2

result = fibonacci(10)
print(*result)