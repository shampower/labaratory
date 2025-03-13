def count_leading_zeros_in_hex(expression_result):
    # Преобразуем число в строку в шестнадцатеричной системе
    hex_value = hex(expression_result)[2:]  # Удаление префикса '0x'
    
    # Проверка наличия ведущих нулей
    leading_zeros = len(hex_value) - len(hex_value.lstrip('0'))
    
    return leading_zeros

# Исходное выражение
expression_result = 3*4**48 + 2*4**43 + 4**20 + 3*4**5 + 2*4**4 + 1

# Проверка наличия значимых нулей
leading_zeros = count_leading_zeros_in_hex(expression_result)

print(f"Результат выражения: {expression_result}")
print(f"В шестнадцатеричной системе: {hex(expression_result)}")
print(f"Количество значимых нулей: {leading_zeros}")