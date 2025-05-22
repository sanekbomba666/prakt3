import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_settings, screen):
        """Initialize alien and set starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load alien image and set its rect Attribute
        self.image = pygame.image.load('alien1.png')
        self.rect = self.image.get_rect()
        
        # Start each alien new the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store Position
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draw alien at current position"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """Move alien right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True