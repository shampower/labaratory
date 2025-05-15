

# @property
это декоратор в Python, который позволяет превратить метод класса в атрибут, доступный для чтения. Он используется для управления доступом к атрибутам объекта, добавляя логику при их получении, установке или удалении. ------Зачем нужен @property? .Контроль доступа к атрибутам .Можно добавить проверки перед установкой значения (например, запретить отрицательные числа). .Можно вычислять значение "на лету" при обращении к атрибуту. .Сокрытие внутренней реализации .Позволяет изменить способ хранения данных, не ломая внешний код. .Создание "вычисляемых" атрибутов .Например, можно сделать атрибут full_name, который объединяет first_name и last_name.

-------.setter — это способ контролировать изменение атрибута в Python. Он работает вместе с @property, позволяя проверять или обрабатывать новое значение перед записью. Например, можно запретить отрицательные числа или автоматически пересчитывать связанные данные.

Короче:

Ставишь @property — чтобы атрибут можно было читать.

Добавляешь @x.setter — чтобы проверять или изменять значение перед сохранением.

Используешь как обычный атрибут — но с логикой внутри.

----@property делает методы похожими на атрибуты. Позволяет добавлять логику при чтении/записи атрибутов. Состоит из трёх частей: геттер, сеттер, делитер (но последние два не обязательны). Используется для инкапсуляции и валидации данных. -----пример в коде Геттер (fabric_price) — возвращает значение _fabric_price. Сеттер — проверяет, что цена ткани не отрицательная, иначе вызывает ошибку.

h__init__
это специальная функция, которая вызывается при создании нового объекта класса. Она также известна как конструктор класса. Это место, где обычно устанавливаются начальные значения атрибутов класса. self — это ссылка на текущий экземпляр класса. Это способ обращения к атрибутам и методам класса изнутри самого класса.

В примере выше, self.color = color устанавливает атрибут color текущего объекта класса Car в значение color, переданное в h__init__.

Следует отметить, что self не передается при создании нового объекта класса. Python автоматически передает ссылку на текущий объект в self.

# Создание абстрактного базового класса
Файл: base_storage.py

    from abc import ABC, abstractmethod

    class StorageDevice(ABC):  # Наследование от ABC
        def __init__(self, name, price, capacity_gb):
            self._name = name
            self._price = price
            self._capacity_gb = capacity_gb

        # Объявление абстрактных методов
        @abstractmethod
        def get_read_speed(self):
            pass

        @abstractmethod
        def get_write_speed(self):
            pass
Что это означает:

Класс наследуется от ABC (Abstract Base Class), что делает его абстрактным.

Методы get_read_speed и get_write_speed помечены декоратором @abstractmethod.

Любой класс-наследник обязан реализовать эти методы, иначе при создании экземпляра возникнет ошибка TypeError.

2. Реализация абстрактных методов в дочерних классах
Пример для класса HDD (файл concrete_devices.py):

    class HDD(StorageDevice):  # Наследование от абстрактного класса
        def __init__(self, name, price, capacity_gb, rpm=7200):
            super().__init__(name, price, capacity_gb)
            self._rpm = rpm

        # Реализация абстрактных методов
        def get_read_speed(self):
            return 80 + (self.rpm - 5400) * 0.05

        def get_write_speed(self):
            return self.get_read_speed() * 0.9
Особенности:

Класс HDD наследуется от StorageDevice.

Реализует все абстрактные методы базового класса (get_read_speed, get_write_speed).

Если не реализовать хотя бы один абстрактный метод, Python выдаст ошибку:

TypeError: Can't instantiate abstract class HDD with abstract methods get_read_speed, get_write_speed
3. Использование других декораторов
В классе StorageDevice также используются:

a. @property (managed-атрибуты)

    @property
    def name(self):
        return self._name

    @property
    def price_per_gb(self):
        return self.price / self.capacity_gb
Превращают методы в свойства (атрибуты), доступные как device.name.

Обеспечивают контролируемый доступ к приватным полям (например, _name).

b. @total_ordering (декоратор сравнений)

    from functools import total_ordering

    @total_ordering
    class StorageDevice(ABC):
        def __eq__(self, other):
            # Реализация равенства

        def __lt__(self, other):
            # Реализация "меньше"
Генерирует автоматически все методы сравнения (>, <=, >= и т.д.) на основе __eq__ и __lt__.

4. Запрет инстанцирования абстрактного класса
Попытка создать объект абстрактного класса вызовет ошибку:

python
device = StorageDevice("Test", 100, 500)  # Ошибка!
# TypeError: Can't instantiate abstract class StorageDevice with abstract methods get_read_speed, get_write_speed
Итог
Абстрактный класс:

Служит шаблоном для дочерних классов.

Задает обязательный интерфейс через @abstractmethod.

Не может быть инстанциирован напрямую.

Декораторы:

@abstractmethod — маркирует методы, которые должны быть реализованы в дочерних классах.

@property — создает управляемые атрибуты (managed attributes).

@total_ordering — автоматизирует реализацию операторов сравнения.

# Иерархия ДОЧЕРНИЕ КЛАССЫ

StorageDevice (ABC)
├── HDD
├── SSD
└── FlashDrive
Каждый дочерний класс реализует уникальную логику абстрактных методов.

Этот подход гарантирует:

Единый интерфейс для всех устройств.

Запрет на создание объектов с нереализованными методами.

Легкую расширяемость системы (можно добавить новые типы устройств, соблюдая контракт базового класса).

Общая структура наследования
StorageDevice (ABC)
├── HDD
├── SSD
└── FlashDrive
Каждый дочерний класс:

Наследует все свойства и методы базового класса

Реализует абстрактные методы get_read_speed() и get_write_speed()

Добавляет уникальные атрибуты и методы

Имеет managed-атрибуты через @property

Реализует минимум 2 dunder-метода

1. Базовый класс: StorageDevice
Файл: base_storage.py

    @total_ordering
    class StorageDevice(ABC):
        def __init__(self, name, price, capacity_gb):
            self._name = name
            self._price = price
            self._capacity_gb = capacity_gb

        @property
        def name(self):
            return self._name

        @property
        def price_per_gb(self):
            return self.price / self.capacity_gb

        @abstractmethod
        def get_read_speed(self): ...

        @abstractmethod
        def get_write_speed(self): ...

        # Dunder-методы
        def __eq__(self, other): ...
        def __lt__(self, other): ...
        def __repr__(self): ...
        def __str__(self): ...
Роль в иерархии:

Определяет общий интерфейс для всех устройств

Задаёт обязательные методы через @abstractmethod

Реализует базовую логику (цена за ГБ, сравнение устройств)

Содержит общие атрибуты:

name (название)

price (цена)

capacity_gb (ёмкость)

2. Дочерний класс: HDD
Файл: concrete_devices.py


    class HDD(StorageDevice):
        def __init__(self, name, price, capacity_gb, rpm=7200):
            super().__init__(name, price, capacity_gb)  # Вызов родительского конструктора
            self._rpm = rpm  # Уникальный атрибут

        @property
        def rpm(self):  # Managed-атрибут
            return self._rpm

        # Реализация абстрактных методов
        def get_read_speed(self):
            return 80 + (self.rpm - 5400) * 0.05

        def get_write_speed(self):
            return self.get_read_speed() * 0.9

        # Dunder-методы
        def __add__(self, other):  # RAID-массив
            return HDD(...)

        def __mul__(self, factor):  # Массив дисков
            return HDD(...)
Особенности:

Добавляет новый параметр rpm (обороты в минуту)

Managed-атрибуты:

rpm (только для чтения)

Уникальная логика:

Расчёт скорости на основе RPM

Dunder-методы:

__add__ — создание RAID-массива

__mul__ — масштабирование массива

3. Дочерний класс: SSD
Файл: concrete_devices.py

    class SSD(StorageDevice):
        def __init__(self, name, price, capacity_gb, nvme=False):
            super().__init__(name, price, capacity_gb)
            self._nvme = nvme  # Уникальный атрибут

        @property
        def is_nvme(self):  # Managed-атрибут
            return self._nvme

        # Реализация абстрактных методов
        def get_read_speed(self):
            return 3500 if self.is_nvme else 550

        def get_write_speed(self):
            return 3000 if self.is_nvme else 500

        # Dunder-методы
        def __contains__(self, tech):  # Проверка технологии
            return tech in {'NVMe', 'SATA'}

        def __call__(self, op_type):  # Вызов как функции
            return self.get_read_speed() if op_type == 'read' else self.get_write_speed()
Особенности:

Добавляет параметр nvme (тип подключения)

Managed-атрибуты:

is_nvme (проверка типа)

Уникальная логика:

Скорость зависит от NVMe/SATA

Dunder-методы:

__contains__ — проверка поддержки технологии

__call__ — вызов объекта как функции

4. Дочерний класс: FlashDrive
Файл: concrete_devices.py

    class FlashDrive(StorageDevice):
        def __init__(self, name, price, capacity_gb, usb_version=3):
            super().__init__(name, price, capacity_gb)
            self._usb_version = usb_version  # Уникальный атрибут

        @property
        def usb_version(self):  # Managed-атрибут
            return self._usb_version

        # Реализация абстрактных методов
        def get_read_speed(self):
            return {2:30, 3:150, 3.1:300, 3.2:500}.get(self.usb_version, 50)

        def get_write_speed(self):
            return self.get_read_speed() * 0.7

        # Dunder-методы
        def __len__(self):  # "Длина" как ёмкость
            return self.capacity_gb

        def __getitem__(self, key):  # Доступ через []
            if key == 'speed':
                return (self.get_read_speed(), self.get_write_speed())
            raise KeyError(...)
Особенности:

Добавляет параметр usb_version (версия USB)

Managed-атрибуты:

usb_version (только для чтения)

Уникальная логика:

Скорость зависит от версии USB

Dunder-методы:

__len__ — возвращает ёмкость

__getitem__ — доступ к данным через ключи

Ключевые принципы иерархии
Единый интерфейс:

Все устройства имеют get_read_speed() и get_write_speed()

Общие свойства: name, price, capacity_gb

Полиморфизм:

python
devices = [HDD(...), SSD(...), FlashDrive(...)]
for device in devices:
    print(device.get_read_speed())  # Вызовется своя реализация для каждого типа
Расширяемость:

Можно добавить новый тип устройства (например, NVMeSSD), унаследовав от StorageDevice

Инкапсуляция:

Все атрибуты защищены (начинаются с _)

Доступ через @property

Совместимость:

Любое устройство можно передать в StorageCalculator

Гарантируется наличие нужных методов и свойств

Итог
Иерархия наследования позволяет:

Управлять сложностью через абстракции

Переиспользовать общую логику

Гарантировать единый интерфейс для всех устройств

Легко добавлять новые типы устройств

Использовать полиморфизм для универсальной обработки объектов

Каждый класс в иерархии:

Специализируется на своей предметной области

Расширяет базовый функционал

Сохраняет совместимость с другими компонентами системы

