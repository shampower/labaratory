def find_divisors_ending_with_7(n):
    """Функция находит все делители числа n, оканчивающиеся на 7."""
    divisors = []
    for i in range(17, int(n**0.5)+1, 10):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

def main():
    found_count = 0
    number = 600001
    while True:
        if found_count >= 5:
            break
        
        divisors = find_divisors_ending_with_7(number)
        valid_divisors = [d for d in divisors if d > 7 and d != number]
        
        if valid_divisors:
            print(f"{number} {min(valid_divisors)}")
            found_count += 1
            
        number += 1

if __name__ == "__main__":
    main()