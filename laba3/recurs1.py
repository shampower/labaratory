def k_permutations_recursive(elements, k):
    if k == 0:
        return [[]]
    
    permutations = []
    for i in range(len(elements)):
        current_element = elements[i]
        remaining_elements = elements[:i] + elements[i+1:]
        for p in k_permutations_recursive(remaining_elements, k - 1):
            permutations.append([current_element] + p)
    
    return permutations
from itertools import permutations

def k_permutations_iterative(elements, k):
    return [list(p) for p in permutations(elements, k)]
elements = [1, 2, 3]
k = 2

print("Рекурсивный подход:")
print(k_permutations_recursive(elements, k))

print("Итеративный подход:")
print(k_permutations_iterative(elements, k))