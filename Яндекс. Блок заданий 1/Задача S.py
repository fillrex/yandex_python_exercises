name = input()
price = int(input())
weight = int(input())
money = int(input())

price_string = f"{weight}кг * {price}руб/кг"
price_format = f"{price_string:>29}"

print(f'''================Чек================
Товар: {name:>28}
Цена: {price_format}
Итого: {price*weight:25}руб
Внесено: {money:23}руб
Сдача: {money - (price*weight):25}руб
===================================''')