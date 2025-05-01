import tkinter as tk # Бібліотека для створення вікон, кнопок, полів вводу
from tkinter import messagebox # Просте вікно для повідомлень(Успіх або помилка)
import ast # Безпечний парсер: перетворює текст в числа, списки, кортежі тощо
import subprocess # Запускатиме гру, як окремий процесс
import importlib # Динамічний імпорт модулів по імені чи шляху
import importlib.util # Утіліти для завантаження модуля з файлу
import pathlib # Зручна робота з файловим шляхом

# Шлях до файлу з налаштуваннями гри
settings_path = pathlib.Path("OOP/settings.py")

def load_settings() -> dict:
    """
    Читаємо settings.py і повертаємо всі його змінні.
    Кроки:
     1. Створюємо опис, звідки і як імпортувати файл.
     2. Створюємо 'порожній' модуль за цим описом.
     3. Виконуємо код файлу всередині.
     4. Перебираємо усі атрибути. Відкидаємо внутрішні з _.
    """
    #  Готуємо "Шаблон" для імпорту модуля з конкретного шляху
    spec = importlib.util.spec_from_file_location("game_settings", settings_path)
    # Створюємо новий порожній модуль
    settings_mod = importlib.util.module_from_spec(spec)
    # Виконуємо код файлу у цьому модулі
    spec.loader.exec_module(settings_mod)

    settings_dict = {}

    # Збираємо усі публічні атрибути в словник
    for name in dir(settings_mod):
        if not name.startswith('_'):
            # getattr - дістає значення змінної за її назвою
            settings_dict[name] = getattr(settings_mod, name)
    return settings_dict

class SettingsLauncher(tk.Tk):
    def __init__(self):
        super().__init__() # Викликаємо конструктор батьківського класу
        self.title("Launcher - Налаштування") # Заголовок вікна
        self.geometry("600x700") # Розмір вікна: ширина x висота

        # Якщо файл існує, підвантажуємо із нього налаштування
        if settings_path.exists():
            self.current_settings = load_settings()
        else:
            # Інакше - порожній словник
            self.current_settings = {}
        # Тут будемо зберігати поля вводу для кожної константи
        self.entries = {}
        # Малюємо всі кнопки та поля
        self.create_widgets()

    def create_widgets(self):
        """
        Малюємо у вікні:
            - Заголовок
            - Рядок для кожного налаштування: назва і поле вводу
            - Кнопки: "Зберегти" і "Запустити гру"
        """
        # Простий текст зверху
        tk.Label(self, text="Налаштування гри", font=("Arial", 14)).pack(pady=10)
        # Контейнер для полів налаштуваннь
        frame = tk.Frame(self)
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Для кожного параметра робимо рядок
        for row, (key, value) in enumerate(self.current_settings.items()):
            # Підпис
            tk.Label(frame, text=key).grid(row=row, column=0, sticky="w",
                                           padx=5, pady=5)
            # Поле вводу, куди вставляємо поточне значення
            entry = tk.Entry(frame, width=40)

if __name__ == "__main__":
    SettingsLauncher().mainloop()

