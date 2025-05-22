import pygame
from pygame.sprite import Sprite

class Boss(Sprite):
    """A class to represent the final boss"""
    
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load boss image
        self.image = pygame.image.load('alien2.png')
        self.rect = self.image.get_rect()
        
        # Start position
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.top = 20
        
        # Boss stats
        self.max_hp = 1000
        self.current_hp = self.max_hp
        self.speed_x = 1
        self.speed_y = 0.5  # Скорость вертикального движения
        self.direction_x = 1  # 1 - вправо, -1 - влево
        self.direction_y = 1  # 1 - вниз, -1 - вверх
        self.move_counter = 0
        self.move_pattern = [
            (1, 1),   # Вправо-вниз
            (-1, 1),  # Влево-вниз
            (-1, -1), # Влево-вверх
            (1, -1)   # Вправо-вверх
        ]
        self.current_pattern = 0
        
        # Store position as float for smooth movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def update(self):
        """Move the boss in complex pattern"""
        # Меняем направление каждые 100 кадров
        self.move_counter += 1
        if self.move_counter >= 100:
            self.move_counter = 0
            self.current_pattern = (self.current_pattern + 1) % len(self.move_pattern)
            self.direction_x, self.direction_y = self.move_pattern[self.current_pattern]
        
        # Движение
        self.x += (self.speed_x * self.direction_x)
        self.y += (self.speed_y * self.direction_y)
        
        # Ограничение движения по экрану
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            self.direction_x = -1
        elif self.rect.left <= 0:
            self.direction_x = 1
            
        if self.rect.top <= 20:  # Верхняя граница
            self.direction_y = 1
        elif self.rect.bottom >= screen_rect.centery:  # Нижняя граница (до середины экрана)
            self.direction_y = -1
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        
    def blitme(self):
        """Draw the boss and its health bar"""
        self.screen.blit(self.image, self.rect)
        self.draw_health_bar()

        
    def draw_health_bar(self):
        """Draw health bar above boss"""
        bar_length = 200
        bar_height = 20
        fill = (self.current_hp / self.max_hp) * bar_length
        
        outline_rect = pygame.Rect(self.rect.centerx - bar_length/2, 
                                 self.rect.top - bar_height - 5, 
                                 bar_length, bar_height)
        fill_rect = pygame.Rect(self.rect.centerx - bar_length/2, 
                               self.rect.top - bar_height - 5, 
                               fill, bar_height)
        
        pygame.draw.rect(self.screen, (255, 0, 0), fill_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), outline_rect, 2)