# Радиус круга
radius = 42

# Площадь круга
area = 3.1415926 * radius ** 2
print(round(area, 4))

# Проверяем, находится ли точка внутри круга
def is_point_in_circle(point, radius):
    x, y = point
    distance_from_origin = (x ** 2 + y ** 2) ** 0.5
    return distance_from_origin <= radius

# Первая точка
point_1 = (23, 34)
if is_point_in_circle(point_1, radius):
    print(True)
else:
    print(False)

# Вторая точка
point_2 = (30, 30)
if is_point_in_circle(point_2, radius):
    print(True)
else:
    print(False)

