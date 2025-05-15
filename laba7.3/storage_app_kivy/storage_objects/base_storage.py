from abc import ABC, abstractmethod
from functools import total_ordering

@total_ordering
class StorageDevice(ABC):
    """Абстрактный базовый класс для устройств хранения"""
    
    def __init__(self, name, price, capacity_gb):
        self._name = name
        self._price = price
        self._capacity_gb = capacity_gb
        
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def capacity_gb(self):
        return self._capacity_gb
    
    @property
    def price_per_gb(self):
        if self.capacity_gb <= 0:
            raise ValueError("Емкость должна быть больше нуля")
        return self.price / self.capacity_gb
    
    @abstractmethod
    def get_read_speed(self):
        pass
    
    @abstractmethod
    def get_write_speed(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, StorageDevice):
            return NotImplemented
        return self.price_per_gb == other.price_per_gb
    
    def __lt__(self, other):
        if not isinstance(other, StorageDevice):
            return NotImplemented
        return self.price_per_gb < other.price_per_gb
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self._name!r}, {self._price}, {self._capacity_gb})"
    
    def __str__(self):
        return f"{self._name} ({self.capacity_gb}GB, {self.price} руб)"