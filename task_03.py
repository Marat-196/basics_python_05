# 3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int,
# премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии
import decimal

n = ['Sergey', 'Nikita', 'Michail']
b = [10_000, 20_000, 17_000]
r = ['25.25%', '10.14%', '14.5%']

dct = {name: round(bets * ((decimal.Decimal(reward.replace('%', ''))) / 100), 2) + bets for name, bets, reward in
       zip(n, b, r)}

print(dct)
