# -*- coding: utf-8 -*-

# Список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Добавляем медведя (bear) между львом и кенгуру
zoo.insert(1, 'bear')
print(zoo)

# Добавляем птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
zoo.extend(birds)
print(zoo)

# Убираем слона
zoo.remove('elephant')
print(zoo)

# Определяем номера клеток для льва и жаворонка
lion_index = zoo.index('lion') + 1
lark_index = zoo.index('lark') + 1
print(f'Лев (lion) сидит в клетке №{lion_index}')
print(f'Жаворонок (lark) сидит в клетке №{lark_index}')
