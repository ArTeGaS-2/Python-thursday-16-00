import random # Імпортуємо модуль для випадкових чисел

def play_game():
    
    secret_number = random.randint(1, 100) # Загадуємо число

    # Поточна кількість спроб
    attempts = 0

    # Максимальна кількість спроб
    max_attempts = 7

    # print(secret_number)

    guess = None

    while guess != secret_number and attempts < (max_attempts + 1):

        attempts += 1

        # Отримуємо число від гравця
        guess = int(input("Введіть число від 1 до 100: \n"))

        # Перевіряє умову (чи меньше загадане число ніж введене)
        if guess < secret_number:
            print(f"Загадане число більше! Поточна спроба - {attempts}")

        # Якщо перша умова не є вірною, перевіряє наступну
        elif guess > secret_number:
            print(f"Загадане число менше! Поточна спроба - {attempts}")

        # Якщо умова не вірна, виконується у всіх інших випадках
        else:
            print(f"Вітаю, ви виграли за {attempts} спроб!")
    
    # Перевіряє чи вгадане було число
    if guess != secret_number:
        # Виконуєься, коли перериваєтся цикл
        print(f"Ви не вгадали число за {max_attempts} спроб. Загадане число {secret_number}.")

# Змінна що індикує, чи згоден гравець грати ще
play_again = 'так'

# Основний ігровий цикл
while play_again.lower() == 'так':
    # Функція, що виконує основну ігрову логіку
    play_game()
    # Робить запит на повторення гри
    play_again = input("Бажаєте зіграти ще? (так/ні)")