# Класс об'єкту - Контейнер для методів і змінних
# що уособлюють собою якийсь абстрактний або реальний
# об'єкт
class ConspectClass:
    def __init__(self):
        # Метод __init__ - конструктор класу. Є на початку
        # кожного класу. Потрібен для створення екземплярів
        self.a = 2 # Ціле число
        self.b = 4.3 # Дробове число
        self.logic = True # Логічна змінна
        self.tempList = [3,6,4,4] # Список
        pass
    def Operators(self):
        # Математичні оператори
        c = self.a + self.b # Додавання
        c = self.a - self.b # Віднімання
        c = self.a * self.b # Множення
        c = self.a / self.b # Ділення

        # Порівняльні або логічні оператори
        if self.a > self.b: # a більше за b
            pass
        if self.a < self.b: # a меньше за b
            pass
        if self.a >= self.b: # a більше або дорівнює
            pass
        if self.a <= self.b: # a більше або дорівнює
            pass
        if self.a == self.b: # Порівнюємо чи дорівнюють
            pass
        if self.a != self.b: # Перевіряємо щоб не дорівнювало
            pass

        # Логічний оператор "and" перевіряє виконання двох
        # або більше умов
        if self.a == self.b and self.logic:
            pass

        # Логічний оператор "or" перевіряє виконання однієї
        # з умов
        if self.a == self.b or self.logic:
            pass



