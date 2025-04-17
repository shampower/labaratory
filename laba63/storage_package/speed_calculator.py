def calculate_transfer_time(data_size_gb, speed_mbs, operation='read'):
    """
    Рассчитывает время передачи данных для устройства хранения
    :param data_size_gb: объем данных в ГБ
    :param speed_mbs: скорость устройства в МБ/с
    :param operation: 'read' или 'write' (чтение/запись)
    :return: время в секундах
    """
    if speed_mbs <= 0:
        raise ValueError("Скорость должна быть положительным числом")
    
    data_size_mb = data_size_gb * 1024  # Конвертируем ГБ в МБ
    time_seconds = data_size_mb / speed_mbs
    
    return time_seconds
