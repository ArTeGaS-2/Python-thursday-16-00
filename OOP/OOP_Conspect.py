class ConspectClass:
    def __init__(self):
        self.a = 2
        self.b = 4
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

