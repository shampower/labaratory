import math

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

def distance(city1, city2):
    # Вычисляем расстояние между двумя городами
    x1, y1 = sites[city1]
    x2, y2 = sites[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Создаем пустой словарь для хранения расстояний
distances = {}

for city1 in sites:
    distances[city1] = {}  # Для каждого города создаем подсловарь
    for city2 in sites:
        if city1 != city2:  # Избегаем дублирования и расстояний до самого себя
            distances[city1][city2] = round(distance(city1, city2), 2)

print(distances)


