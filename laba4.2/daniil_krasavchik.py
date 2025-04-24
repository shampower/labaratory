import time
import functools
from math import sqrt

## ==============================================
## 1. Декоратор для ограничения времени выполнения
## ==============================================

def time_limit(seconds):
    """Декоратор, ограничивающий время выполнения функции"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time
            
            if elapsed > seconds:
                raise TimeoutError(f"Функция {func.__name__} выполнялась {elapsed:.2f} сек (лимит: {seconds} сек)")
            return result
        return wrapper
    return decorator

## ==============================================
## 2. Замыкание для проверки простых чисел
## ==============================================

def make_prime_checker():
    """Создает замыкание для проверки простых чисел с кэшированием"""
    primes_cache = [2, 3]  # Кэш известных простых чисел
    
    def is_prime(n):
        """Проверяет, является ли число простым"""
        if n <= 1:
            return False
        if n in primes_cache:
            return True
        if any(n % p == 0 for p in primes_cache):
            return False
        
        # Проверяем делители до √n
        max_divisor = int(sqrt(n)) + 1
        for i in range(primes_cache[-1] + 2, max_divisor, 2):
            if is_prime(i) and n % i == 0:
                return False
        
        primes_cache.append(n)
        return True
    
    return is_prime

# Создаем экземпляр замыкания
is_prime = make_prime_checker()

## ==============================================
## 3. Функции для вычисления перестановок
## ==============================================

@time_limit(1)
def k_permutations_recursive(elements, k):
    """Рекурсивная генерация перестановок длины k"""
    if k == 0:
        return [[]]
    
    result = []
    for i in range(len(elements)):
        current = elements[i]
        remaining = elements[:i] + elements[i+1:]
        for p in k_permutations_recursive(remaining, k-1):
            result.append([current] + p)
    
    return result

@time_limit(1)
def k_permutations_iterative(elements, k):
    """Итеративная генерация перестановок длины k"""
    result = []
    n = len(elements)
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

## ==============================================
## 4. Функции для вычисления последовательности
## ==============================================

@time_limit(1)
def sequence_recursive(i):
    """Рекурсивное вычисление последовательности"""
    if i == 0:
        return 0
    prev = sequence_recursive(i-1)
    term = 1/i if is_prime(i) else 1/(i**2)
    return i * prev + term

@time_limit(1)
def sequence_iterative(i):
    """Итеративное вычисление последовательности"""
    if i == 0:
        return 0
    x = 0
    for n in range(1, i+1):
        term = 1/n if is_prime(n) else 1/(n**2)
        x = n * x + term
    return x

## ==============================================
## 5. Примеры использования и тестирование
## ==============================================

if __name__ == "__main__":
    print("1. Тест перестановок:")
    elements = [1, 2, 3]
    k = 2
    print(f"Рекурсивные перестановки из {elements} длиной {k}:")
    print(k_permutations_recursive(elements, k))
    print(f"Итеративные перестановки из {elements} длиной {k}:")
    print(k_permutations_iterative(elements, k))
    
    print("\n2. Тест последовательности:")
    n = 5
    print(f"Последовательность (рекурсивно) для n={n}:")
    print(sequence_recursive(n))
    print(f"Последовательность (итеративно) для n={n}:")
    print(sequence_iterative(n))
    
    print("\n3. Тест проверки простых чисел:")
    print("Простые числа до 20:")
    print([x for x in range(20) if is_prime(x)])
    
    print("\n4. Тест ограничения времени:")
    try:
        print("Попытка вычисления перестановок для большого n...")
        print(k_permutations_recursive(list(range(12)), 10))
    except TimeoutError as e:
        print("Ошибка:", e)
