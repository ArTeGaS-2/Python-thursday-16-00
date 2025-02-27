import pygame

class Button:
    """Базова кнопка: завантажує зображення, малює, перевіряє клік"""
    def __init__(self, image_path, pos):
        # Завантажує зображення
        self.image = pygame.image.load(image_path).convert_alpha()
        # Створюємо прямокутник кнопки (Rect)
        self.rect = self.image.get_rect()
        # Встановлюємо позицію
        self.rect.topleft = pos

    def draw(self, screen):
        """Малюємо кнопку на екрані."""
        screen.blit(self.image, self.rect)
    def handle_event(self, event):
        """Обробка подій"""
        pass

# ----|----|----|----|----|----|----|----|----|----|----
    
class PauseButton(Button):
    """Кнопка 'Пауза': змінює self.game_manager.paused """
    def __init__(self, image_path, pos, game_manager):
        super().__init__(image_path, pos)
        self.game_manager = game_manager
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Отримуємо позицію миші і 
            # перевіряємо прямокутник кнопки
            if self.rect.collidepoint(event.pos):
                # Перемикаємо режим паузи
                self.game_manager.paused = not self.game_manager.paused

# ------------------------
                
class ExitButton(Button):
    """Кнопка 'Вихід': при натисканні закриває гру. """
    def __init__(self, image_path, pos):
        super().__init__(image_path, pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                pygame.quit()
                exit()
