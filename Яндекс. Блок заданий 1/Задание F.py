item = input()
price = int(input())
weight = int(input())
money = int(input())
change = int(money - price * weight)
print(f'''Чек
{item} - {weight}кг - {price}руб/кг
Итого: {price * weight}руб
Внесено: {money}руб
Сдача: {change}руб''')