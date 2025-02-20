# -*- coding: utf-8 -*-

# Моя семья
my_family = ["Отец", "Мать", "Сын"]

# Приблизительный рост членов семьи
my_family_height = [
    ["Отец", 180],  # Рост в сантиметрах
    ["Мать", 165],
    ["Сын", 170],
]

# Найти рост отца
father_height = next(item[1] for item in my_family_height if item[0] == "Отец")
print(f'Рост отца - {father_height} см')

# Посчитать общий рост всей семьи
total_height = sum(height for _, height in my_family_height)
print(f'Общий рост моей семьи - {total_height} см')