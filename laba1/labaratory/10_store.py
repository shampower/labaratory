# Определение словарей
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Расчёт стоимости товаров
def calculate_cost(goods_dict, store_dict):
    result = {}
    for item, code in goods_dict.items():
        total_quantity = 0
        total_cost = 0
        for entry in store_dict[code]:
            quantity = entry['quantity']
            price = entry['price']
            total_quantity += quantity
            total_cost += quantity * price
        result[item] = (total_quantity, total_cost)
    return result

costs = calculate_cost(goods, store)

# Вывод результатов
for item, (quantity, cost) in costs.items():
    print(f'{item} - {quantity} шт, стоимость {cost} руб')