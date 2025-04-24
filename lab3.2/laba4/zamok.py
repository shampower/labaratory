import time
import math
from functools import wraps

# Декоратор для ограничения времени выполнения
def time_limit(limit):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed_time = time.time() - start_time

            if elapsed_time > limit:
                raise TimeoutError(f"Функция выполнялась дольше {limit} секунд.")
            return result
        return wrapper
    return decorator

# Замыкание для генерации простых чисел
def prime_generator():
    primes = []  # Список для хранения найденных простых чисел

    def is_prime(n):
        if n < 2:
            return False
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True

    def get_next_prime():
        num = 2 if not primes else primes[-1] + 1
        while True:
            if is_prime(num):
                primes.append(num)
                return num
            num += 1

    return get_next_prime

# Применяем декоратор к замыканию
@time_limit(5)  # Ограничение времени выполнения: 5 секунд
def get_primes_with_time_limit():
    generator = prime_generator()
    primes = []
    while True:
        primes.append(generator())
        print(f"Найдено простое число: {primes[-1]}")
        time.sleep(1)  # Имитация задержки

# Пример использования
try:
    get_primes_with_time_limit()
except TimeoutError as e:
    print(e)