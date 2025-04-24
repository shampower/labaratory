 # 1. Функция для вычисления всех перестановок списка длиной k

# Рекурсивная реализация
def K_permutations_recursive(elements, k):
    if k == 0:
        return [[]]
    
    result = []
    for i in range(len(elements)):
        current = elements[i]
        remaining = elements[:i] + elements[i+1:]
        for p in K_permutations_recursive(remaining, k-1):
            result.append([current] + p)
    
    return result

# Итеративная реализация (без itertools)
def K_permutations_iterative(elements, k):
    result = []
    n = len(elements)
    
    # Инициализация
    indices = list(range(n))
    cycles = list(range(n, n-k, -1))
    result.append([elements[i] for i in indices[:k]])
    
    while True:
        for i in reversed(range(k)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                result.append([elements[i] for i in indices[:k]])
                break
        else:
            return result


# 2. Функция для вычисления последовательности x_i = i*x_{i-1} + 1/i, x_0 = 0

# Рекурсивная реализация
def sequence_recursive(i):
    if i == 0:
        return 0
    prev = sequence_recursive(i-1)
    return i * prev + 1/i

# Итеративная реализация
def sequence_iterative(i):
    if i == 0:
        return 0
    x = 0
    for n in range(1, i+1):
        x = n * x + 1/n
    return x


# Примеры использования
if __name__ == "__main__":
    print("Перестановки рекурсивно:", K_permutations_recursive([1, 2, 3], 2))
    print("Перестановки итеративно:", K_permutations_iterative([1, 2, 3], 2))
    
    n = 5
    print(f"Последовательность для n={n} рекурсивно:", sequence_recursive(n))
    print(f"Последовательность для n={n} итеративно:", sequence_iterative(n))
