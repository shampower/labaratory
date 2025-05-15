from .base_storage import StorageDevice

class HDD(StorageDevice):
    def __init__(self, name, price, capacity_gb, rpm=7200):
        super().__init__(name, price, capacity_gb)
        self._rpm = rpm
        
    @property
    def rpm(self):
        return self._rpm
    
    def get_read_speed(self):
        return 80 + (self.rpm - 5400) * 0.05
    
    def get_write_speed(self):
        return self.get_read_speed() * 0.9
    
    def __add__(self, other):
        if isinstance(other, HDD):
            return HDD(
                f"RAID0({self.name}+{other.name})",
                self.price + other.price,
                self.capacity_gb + other.capacity_gb,
                (self.rpm + other.rpm) // 2
            )
        return NotImplemented
    
    def __mul__(self, factor):
        if isinstance(factor, int) and factor > 1:
            return HDD(
                f"Array{factor}_{self.name}",
                self.price * factor,
                self.capacity_gb * factor,
                self.rpm
            )
        return NotImplemented

class SSD(StorageDevice):
    def __init__(self, name, price, capacity_gb, nvme=False):
        super().__init__(name, price, capacity_gb)
        self._nvme = nvme
        
    @property
    def is_nvme(self):
        return self._nvme
    
    def get_read_speed(self):
        return 3500 if self.is_nvme else 550
    
    def get_write_speed(self):
        return 3000 if self.is_nvme else 500
    
    def __contains__(self, tech):
        techs = {'NVMe': self.is_nvme, 'SATA': not self.is_nvme}
        return techs.get(tech, False)
    
    def __call__(self, op_type):
        if op_type == 'read':
            return self.get_read_speed()
        elif op_type == 'write':
            return self.get_write_speed()
        raise ValueError("Неизвестная операция")

class FlashDrive(StorageDevice):
    def __init__(self, name, price, capacity_gb, usb_version=3):
        super().__init__(name, price, capacity_gb)
        self._usb_version = usb_version
        
    @property
    def usb_version(self):
        return self._usb_version
    
    def get_read_speed(self):
        speed_map = {2: 30, 3: 150, 3.1: 300, 3.2: 500}
        return speed_map.get(self.usb_version, 50)
    
    def get_write_speed(self):
        return self.get_read_speed() * 0.7
    
    def __len__(self):
        return self.capacity_gb
    
    def __getitem__(self, key):
        if key == 'speed':
            return (self.get_read_speed(), self.get_write_speed())
        raise KeyError(f"Неизвестный ключ: {key}")