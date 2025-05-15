from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.metrics import dp
from openpyxl import Workbook

from storage_objects.concrete_devices import HDD, SSD, FlashDrive
from storage_objects.calculator import StorageCalculator

class StorageApp(App):
    def build(self):
        devices = [
            HDD("Seagate HDD", 4000, 2000, 7200),
            SSD("Samsung SSD", 8000, 1000),
            FlashDrive("Kingston Flash", 1500, 256, 3.2)
        ]
        self.calculator = StorageCalculator(devices)
        return MainLayout(calculator=self.calculator)

class MainLayout(BoxLayout):
    def __init__(self, calculator, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(10)
        self.spacing = dp(5)
        self.calculator = calculator
        self.last_results = None

        # Ввод данных
        input_grid = BoxLayout(size_hint_y=None, height=dp(80))
        self.data_input = TextInput(text='100', input_filter='float')
        self.operation_spinner = Spinner(
            values=['read', 'write'],
            text='read'
        )
        input_grid.add_widget(Label(text='Объем (ГБ):'))
        input_grid.add_widget(self.data_input)
        input_grid.add_widget(Label(text='Операция:'))
        input_grid.add_widget(self.operation_spinner)
        self.add_widget(input_grid)

        # Кнопки
        btn_box = BoxLayout(size_hint_y=None, height=dp(50))
        btn_box.add_widget(Button(
            text='Рассчитать',
            on_press=self.calculate
        ))
        btn_box.add_widget(Button(
            text='Устройства',
            on_press=self.show_devices
        ))
        btn_box.add_widget(Button(
            text='Сохранить в Excel',
            on_press=self.save_to_excel
        ))
        self.add_widget(btn_box)

        # Результаты
        self.results = Label(
            text='Здесь будут результаты',
            size_hint_y=None,
            text_size=(None, None),
            valign='top'
        )
        scroll = ScrollView()
        scroll.add_widget(self.results)
        self.add_widget(scroll)

    def calculate(self, instance):
        try:
            data = float(self.data_input.text)
            if data <= 0:
                raise ValueError("Объем должен быть > 0")
            
            op = self.operation_spinner.text
            self.last_results = self.calculator(data, op)
            
            text = "[b]Результаты:[/b]\n\n"
            text += f"Данные: {data} ГБ, операция: {op}\n\n"
            
            text += "[b]Все устройства:[/b]\n"
            for res in self.last_results['all']:
                dev = res['device']
                text += (
                    f"{dev.name}: {res['time']} сек, "
                    f"{res['price']} руб\n"
                )
            
            text += "\n[b]Лучшие:[/b]\n"
            text += f"Быстрее: {self.last_results['fastest']['device'].name} ({self.last_results['fastest']['time']} сек)\n"
            text += f"Дешевле: {self.last_results['cheapest']['device'].name} ({self.last_results['cheapest']['price_per_gb']} руб/ГБ)"
            
            self.results.text = text
            
        except Exception as e:
            self.show_popup(f"Ошибка: {str(e)}")

    def save_to_excel(self, instance):
        if not self.last_results:
            self.show_popup("Сначала выполните расчет!")
            return
        
        try:
            wb = Workbook()
            ws = wb.active
            ws.title = "Сравнение устройств"

            # Заголовки
            headers = ["Устройство", "Время (сек)", "Цена за ГБ", "Общая стоимость"]
            ws.append(headers)

            # Данные
            for res in self.last_results['all']:
                ws.append([
                    res['device'].name,
                    res['time'],
                    res['price_per_gb'],
                    res['price']
                ])

            # Лучшие варианты
            ws.append([])
            ws.append(["Самое быстрое устройство:", 
                      self.last_results['fastest']['device'].name,
                      self.last_results['fastest']['time']])
            ws.append(["Самое экономичное устройство:", 
                      self.last_results['cheapest']['device'].name,
                      self.last_results['cheapest']['price_per_gb']])

            filename = "storage_report.xlsx"
            wb.save(filename)
            self.show_popup(f"Файл {filename} успешно сохранен!")

        except Exception as e:
            self.show_popup(f"Ошибка сохранения: {str(e)}")

    def show_devices(self, instance):
        text = "[b]Доступные устройства:[/b]\n\n"
        for dev in self.calculator:
            text += (
                f"{dev.name}\n"
                f"Тип: {type(dev).__name__}\n"
                f"Скорость: {dev.get_read_speed()}/{dev.get_write_speed()} МБ/с\n"
                f"Цена: {dev.price} руб за {dev.capacity_gb} ГБ\n\n"
            )
        self.show_popup(text, title="Устройства", size=(400, 300))

    def show_popup(self, message, title="Информация", size=(300, 200)):
        content = Label(text=message, padding=dp(10))
        popup = Popup(
            title=title,
            content=content,
            size_hint=(None, None),
            size=size
        )
        popup.open()

if __name__ == '__main__':
    StorageApp().run()