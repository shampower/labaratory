# Задание

Составить словарь словарей и найти расстояние между городами.

## Описание 
Функция для вычисления всех перестановок списка длиной k

## Решение
Рекурсивные реализации:

Используют вызовы самой себя.

Имеют базовый случай для остановки рекурсии.

Могут быть менее эффективны для больших i или k из-за переполнения стека.

Итеративные реализации:

Работают через циклы.

Обычно быстрее и не имеют ограничений на глубину рекурсии.

Могут быть сложнее для понимания (например, алгоритм перестановок).

Все функции не используют глобальные переменные и работают изолированно.

## Итоговый результат:

![image](https://github.com/user-attachments/assets/fdd8b851-bab2-43dc-b4e4-cc53ab14d0fa)


# Cправочные материалы:

## 1. Функции для вычисления перестановок
## 1.1 Рекурсивная реализация K_permutations_recursive(elements, k)
Назначение:
Генерирует все возможные перестановки длины k из списка elements с использованием рекурсии.

Построчное объяснение:

        def K_permutations_recursive(elements, k):
Объявление функции с параметрами:

elements — список элементов, из которых строятся перестановки.

k — длина перестановки.

    if k == 0:
        return [[]]
Базовый случай рекурсии:
Если k = 0, возвращается список с одним пустым списком [[]], так как единственная перестановка длины 0 — пустая.

python
    result = []
Инициализация списка result, в который будут собираться все перестановки.

    for i in range(len(elements)):
Цикл по индексам элементов списка elements.

        current = elements[i]
Выбираем текущий элемент (current) по индексу i.

        remaining = elements[:i] + elements[i+1:]
Формируем новый список remaining, исключая current:

        elements[:i] — все элементы до i.

        elements[i+1:] — все элементы после i.

        for p in K_permutations_recursive(remaining, k-1):
Рекурсивный вызов функции для оставшихся элементов (remaining) и длины k-1.

p — каждая из перестановок длины k-1.

            result.append([current] + p)
Добавляем в result новую перестановку, состоящую из current и перестановки p.

    return result
Возвращаем список всех перестановок.

## 1.2 Итеративная реализация K_permutations_iterative(elements, k)
Назначение:
Генерирует все возможные перестановки длины k из списка elements без рекурсии (итеративно).

Построчное объяснение:

    def K_permutations_iterative(elements, k):
Объявление функции с параметрами elements и k.

    result = []
    n = len(elements)
result — список для хранения перестановок.

n — длина исходного списка.

    indices = list(range(n))
    cycles = list(range(n, n-k, -1))
indices — список индексов [0, 1, 2, ..., n-1].

cycles — список счётчиков для генерации перестановок.
Например, для n=3, k=2 будет [3, 2].

    result.append([elements[i] for i in indices[:k]])
Добавляем первую перестановку (берём первые k элементов из indices).

    while True:
Бесконечный цикл (прерывается внутри при выполнении условия).

        for i in reversed(range(k)):
Цикл в обратном порядке по индексам от k-1 до 0.

            cycles[i] -= 1
Уменьшаем счётчик для текущей позиции i.

            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
Если счётчик cycles[i] достиг нуля:

Сдвигаем индексы (indices[i:] заменяется на хвост списка).

Восстанавливаем cycles[i] до n - i.

            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                result.append([elements[i] for i in indices[:k]])
                break
Если счётчик не ноль:

Меняем местами элементы в indices.

Добавляем новую перестановку в result.

Прерываем цикл for (переходим к следующей итерации while).

        else:
            return result
Если цикл for завершился без break, значит, все перестановки сгенерированы — возвращаем result.

## 2. Функции для вычисления последовательности x_i = i * x_{i-1} + 1/i
## 2.1 Рекурсивная реализация sequence_recursive(i)
Назначение:
Вычисляет x_i по рекуррентной формуле с использованием рекурсии.

Построчное объяснение:

    def sequence_recursive(i):
Объявление функции с параметром i (номер элемента последовательности).

    python
        if i == 0:
            return 0
Базовый случай:
При i = 0 возвращается 0 (по условию x_0 = 0).

    prev = sequence_recursive(i-1)
Рекурсивный вызов для i-1 (предыдущий элемент последовательности).

    return i * prev + 1/i
Вычисление текущего значения по формуле x_i = i * x_{i-1} + 1/i.

## 2.2 Итеративная реализация sequence_iterative(i)
Назначение:
Вычисляет x_i без рекурсии (через цикл).

Построчное объяснение:

    def sequence_iterative(i):
Объявление функции с параметром i.

    if i == 0:
        return 0
Если i = 0, сразу возвращаем 0.

    x = 0
Инициализация начального значения x (это x_0 = 0).

    for n in range(1, i+1):
Цикл от 1 до i включительно.

        x = n * x + 1/n
Вычисление x_n по формуле x_n = n * x_{n-1} + 1/n.

    return x
Возвращаем вычисленное значение x_i.

## Выводы
Рекурсивные реализации:

Используют вызовы самой себя.

Имеют базовый случай для остановки рекурсии.

Могут быть менее эффективны для больших i или k из-за переполнения стека.

Итеративные реализации:

Работают через циклы.

Обычно быстрее и не имеют ограничений на глубину рекурсии.

Могут быть сложнее для понимания (например, алгоритм перестановок).

Все функции не используют глобальные переменные и работают изолированно.


