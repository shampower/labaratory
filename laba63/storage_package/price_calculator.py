def calculate_price_per_gb(price, capacity_gb):
    """
    Рассчитывает цену за 1 ГБ памяти
    :param price: цена устройства
    :param capacity_gb: объем памяти в ГБ
    :return: цена за 1 ГБ
    """
    if capacity_gb <= 0:
        raise ValueError("Объем памяти должен быть положительным числом")
    
    return price / capacity_gb

def calculate_total_price(price_per_gb, data_size_gb):
    """
    Рассчитывает общую стоимость хранения данных
    :param price_per_gb: цена за 1 ГБ
    :param data_size_gb: объем данных в ГБ
    :return: общая стоимость
    """
    return price_per_gb * data_size_gb 
