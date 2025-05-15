class StorageCalculator:
    def __init__(self, devices):
        self.devices = devices
    
    def calculate_time(self, device, data_gb, operation):
        speed = device.get_read_speed() if operation == 'read' else device.get_write_speed()
        return (data_gb * 1024) / speed
    
    def calculate_price(self, device, data_gb):
        return device.price_per_gb * data_gb
    
    def compare(self, data_gb, operation):
        results = []
        for device in self.devices:
            try:
                time = self.calculate_time(device, data_gb, operation)
                price = self.calculate_price(device, data_gb)
                results.append({
                    'device': device,
                    'time': round(time, 2),
                    'price': round(price, 2),
                    'price_per_gb': round(device.price_per_gb, 2)
                })
            except Exception as e:
                print(f"Ошибка для {device.name}: {e}")
        
        fastest = min(results, key=lambda x: x['time'], default=None)
        cheapest = min(results, key=lambda x: x['price_per_gb'], default=None)
        
        return {
            'all': results,
            'fastest': fastest,
            'cheapest': cheapest
        }
    
    def __call__(self, data_gb, operation='read'):
        return self.compare(data_gb, operation)
    
    def __iter__(self):
        return iter(self.devices)