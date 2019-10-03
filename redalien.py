import pygame
import random
from pygame.sprite import Sprite

class RAlien(Sprite):
    def __init__(self, ai_settings, screen):
        super(RAlien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/redalien.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship in the center
        self.rect.right = self.screen_rect.left
        self.rect.y = self.screen_rect.bottom / 10
        # Prep score
        self.font = pygame.font.Font(None, 46)
        self.text = self.font.render("200", 1, (255, 0, 0))
        self.width, self.height = self.font.size("200")
        self.moving_right = False
        self.count = 0

    def update(self, audio):
        # Update ship's center value
        if random.randint(0, 5000) == 0 and not self.moving_right:
            self.moving_right = True
            self.rect.right = self.screen_rect.left
        if self.moving_right:
            self.rect.centerx += self.ai_settings.ship_speed_factor / 10
        if self.rect.left > self.screen_rect.right:
            self.rect.right = self.screen_rect.left
            self.moving_right = False

    def blitme(self):
        # draw ship at current location
        if self.moving_right:
            self.screen.blit(self.image, self.rect)
        elif self.count > 0:
            self.screen.blit(self.text, self.rect)
            self.count -= 1

    def dead(self):
        self.moving_right = False
        self.count = 60
