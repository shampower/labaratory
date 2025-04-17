import tkinter as tk
from tkinter import ttk, messagebox
from openpyxl import Workbook
from storage_package import compare_devices  # Исправлено имя функции

class StorageComparisonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Сравнение устройств хранения")
        self.root.geometry("700x600")
        
        # Стандартные характеристики устройств
        self.devices = [
            {
                'name': 'HDD',
                'read_speed': 120,
                'write_speed': 100,
                'price': 4000,
                'capacity_gb': 1000
            },
            {
                'name': 'SSD',
                'read_speed': 500,
                'write_speed': 450,
                'price': 6000,
                'capacity_gb': 500
            },
            {
                'name': 'Flash',
                'read_speed': 300,
                'write_speed': 200,
                'price': 2000,
                'capacity_gb': 128
            }
        ]
        
        # Переменные для хранения данных
        self.data_size_var = tk.DoubleVar(value=10)
        self.operation_var = tk.StringVar(value='read')
        self.results = []
        
        self.create_widgets()
    
    def create_widgets(self):
        # Ввод данных
        input_frame = ttk.LabelFrame(self.root, text="Параметры расчета")
        input_frame.pack(pady=10, padx=10, fill="x")
        
        # Объем данных
        ttk.Label(input_frame, text="Объем данных (ГБ):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        data_size_entry = ttk.Entry(input_frame, textvariable=self.data_size_var)
        data_size_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Операция
        ttk.Label(input_frame, text="Операция:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        operation_combobox = ttk.Combobox(input_frame, textvariable=self.operation_var, values=['read', 'write'])
        operation_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        operation_combobox.current(0)
        
        # Кнопки
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.calc_button = ttk.Button(
            button_frame, 
            text="Рассчитать", 
            command=self.calculate
        )
        self.calc_button.pack(side="left", padx=5)
        
        self.save_button = ttk.Button(
            button_frame, 
            text="Сохранить в Excel", 
            command=self.save_to_excel,
            state="disabled"
        )
        self.save_button.pack(side="left", padx=5)
        
        # Результаты
        self.result_frame = ttk.LabelFrame(self.root, text="Результаты сравнения")
        self.result_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Таблица результатов
        columns = ("Устройство", "Время (сек)", "Цена за ГБ (руб)", "Общая стоимость (руб)")
        self.result_tree = ttk.Treeview(
            self.result_frame, 
            columns=columns, 
            show="headings",
            height=5
        )
        
        for col in columns:
            self.result_tree.heading(col, text=col)
            self.result_tree.column(col, width=150, anchor="center")
        
        self.result_tree.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Лучшие варианты
        best_frame = ttk.Frame(self.result_frame)
        best_frame.pack(fill="x", pady=10)
        
        # Самый быстрый
        self.fastest_var = tk.StringVar()
        ttk.Label(best_frame, text="Самое быстрое устройство:").pack(side="left", padx=5)
        ttk.Label(best_frame, textvariable=self.fastest_var, font=('Arial', 10, 'bold')).pack(side="left", padx=5)
        
        # Самое экономичное
        self.cheapest_var = tk.StringVar()
        ttk.Label(best_frame, text="Самое экономичное устройство:").pack(side="left", padx=20)
        ttk.Label(best_frame, textvariable=self.cheapest_var, font=('Arial', 10, 'bold')).pack(side="left", padx=5)
    
    def calculate(self):
        """Выполняет расчеты и отображает результаты"""
        try:
            data_size = self.data_size_var.get()
            operation = self.operation_var.get()
            
            if data_size <= 0:
                raise ValueError("Объем данных должен быть положительным числом")
            
            # Выполняем сравнение устройств
            comparison = compare_devices(self.devices, data_size, operation)
            self.results = comparison['all_results']
            
            # Очищаем таблицу
            for item in self.result_tree.get_children():
                self.result_tree.delete(item)
            
            # Проверка наличия результатов
            if not self.results:
                messagebox.showwarning("Предупреждение", "Нет данных для отображения")
                self.save_button.config(state="disabled")
                return
            
            # Заполняем таблицу
            for result in self.results:
                self.result_tree.insert("", "end", values=(
                    result['name'],
                    f"{result['time']:.2f}",
                    f"{result['price_per_gb']:.2f}",
                    f"{result['total_price']:.2f}"
                ))
            
            # Отображаем лучшие варианты
            if comparison['fastest']:
                self.fastest_var.set(
                    f"{comparison['fastest']['name']} ({comparison['fastest']['time']:.2f} сек)"
                )
            else:
                self.fastest_var.set("Не определено")
            
            if comparison['cheapest']:
                self.cheapest_var.set(
                    f"{comparison['cheapest']['name']} ({comparison['cheapest']['price_per_gb']:.2f} руб/ГБ)"
                )
            else:
                self.cheapest_var.set("Не определено")
            
            # Активируем кнопку сохранения
            self.save_button.config(state="normal")
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Некорректные данные: {str(e)}")
            self.save_button.config(state="disabled")
    
    def save_to_excel(self):
        """Сохраняет результаты в файл Excel"""
        try:
            if not self.results:
                messagebox.showwarning("Предупреждение", "Нет данных для сохранения")
                return
            
            wb = Workbook()
            ws = wb.active
            ws.title = "Сравнение устройств"
            
            # Заголовки
            headers = ["Устройство", "Время (сек)", "Цена за ГБ (руб)", "Общая стоимость (руб)"]
            ws.append(headers)
            
            # Данные
            for result in self.results:
                ws.append([
                    result['name'],
                    round(result['time'], 2),
                    round(result['price_per_gb'], 2),
                    round(result['total_price'], 2)
                ])
            
            # Добавляем лучшие варианты
            ws.append([])
            ws.append(["Самое быстрое устройство:", self.fastest_var.get()])
            ws.append(["Самое экономичное устройство:", self.cheapest_var.get()])
            
            # Сохраняем файл
            filename = "storage_comparison.xlsx"
            wb.save(filename)
            messagebox.showinfo("Успех", f"Результаты сохранены в файл {filename}")
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StorageComparisonApp(root)
    root.mainloop()