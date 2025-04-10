def spiral_generator(matrix):
    if not matrix:
        return
    
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Направления: вправо, вниз, влево, вверх
    x, y = rows // 2, cols // 2  # Начинаем с центра
    
    visited = set()
    visited.add((x, y))
    yield (x, y, matrix[x][y])
    
    step_length = 1
    step_count = 0
    direction_index = 0
    
    while True:
        for _ in range(step_length):
            dx, dy = directions[direction_index]
            x += dx
            y += dy
            
            if not (0 <= x < rows and 0 <= y < cols):
                return  # Выход за границы матрицы
            
            if (x, y) not in visited:
                visited.add((x, y))
                yield (x, y, matrix[x][y])
        
        direction_index = (direction_index + 1) % 4
        step_count += 1
        
        if step_count % 2 == 0:
            step_length += 1

def solve(matrix):
    # Фильтруем элементы, у которых чётность элемента совпадает с чётностью суммы индексов
    filtered = filter(lambda item: (item[2] % 2) == ((item[0] + item[1]) % 2), spiral_generator(matrix))
    # Преобразуем в список значений (без индексов)
    result = list(map(lambda item: item[2], filtered))
    return result

# Пример использования:

matrix = [
    [1, 2, 3, 4, 5],
    [6, 8, 8, 9, 10],  # 8 на (1,1) → (1+1)%2=0, 8%2=0 → подходит
    [11, 12, 14, 14, 15],  # 14 на (2,2) → (2+2)%2=0, 14%2=0 → подходит
    [16, 17, 18, 20, 20],
    [21, 22, 23, 24, 25]
]

print(solve(matrix))  # Выведет подходящие элементы