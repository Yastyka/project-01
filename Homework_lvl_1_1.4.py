titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}


for name_prod, code in titles.items():
    total_quantity = 0
    total_price = 0
    for titles in store[code]:
        quantity = 0
        price = 0
        quantity += titles['quantity']
        price += titles['price']
        total_price += quantity * price
        total_quantity += quantity
    print(name_prod, " - ", total_quantity, " шт, ", total_price, " руб")

# Кроссовки тип 3 (Adidas)  -  31  шт,  50747  руб
# Мячик тип 2 (Adidas)  -  14  шт,  660  руб
# Кепка тип 1 (Adidas)  -  60  шт,  17124  руб
# Ремень тип 2 (Nike)  -  9  шт,  1930  руб
# Футболка тип 1 (Adidas)  -  134  шт,  54264  руб
# Шапка тип 5 (Puma)  -  26  шт,  4550  руб