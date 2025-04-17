from .speed_calculator import calculate_transfer_time
from .price_calculator import calculate_price_per_gb, calculate_total_price

def compare_devices(devices, data_size_gb, operation='read'):
    """
    Сравнивает устройства по времени передачи и стоимости
    :param devices: список словарей с характеристиками устройств
    :param data_size_gb: объем данных для передачи
    :param operation: 'read' или 'write'
    :return: словарь с результатами сравнения
    """
    results = []
    
    for device in devices:
        try:
            # Расчет времени
            speed = device.get('read_speed' if operation == 'read' else 'write_speed', 0)
            if speed <= 0:
                continue
                
            time = calculate_transfer_time(data_size_gb, speed)
            
            # Расчет стоимости
            if device.get('price', 0) <= 0 or device.get('capacity_gb', 0) <= 0:
                continue
                
            price_per_gb = calculate_price_per_gb(device['price'], device['capacity_gb'])
            total_price = calculate_total_price(price_per_gb, data_size_gb)
            
            results.append({
                'name': device.get('name', 'Unknown'),
                'time': time,
                'price_per_gb': price_per_gb,
                'total_price': total_price
            })
        except Exception as e:
            print(f"Ошибка при обработке устройства {device.get('name', 'Unknown')}: {str(e)}")
            continue
    
    if not results:
        return {
            'all_results': [],
            'fastest': None,
            'cheapest': None
        }
    
    # Сортируем по времени и стоимости
    fastest = min(results, key=lambda x: x['time'], default=None)
    cheapest = min(results, key=lambda x: x['price_per_gb'], default=None)
    
    return {
        'all_results': results,
        'fastest': fastest,
        'cheapest': cheapest
    }