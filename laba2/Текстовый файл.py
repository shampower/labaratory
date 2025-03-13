# Количество букв для выбора после фиксирования буквы 'К'
n_letters = 5

# Возможные варианты для первой и второй позиции
first_position_options = n_letters
second_position_options = n_letters

# Количество вариантов для положения буквы 'К' (первая, вторая или третья)
k_positions = 3

# Общее количество комбинаций
total_combinations = k_positions * first_position_options * second_position_options

print(total_combinations) 
