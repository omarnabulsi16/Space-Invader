import pygame
from pygame.sprite import Sprite

class Bunker(Sprite):
    def __init__(self, ai_settings, screen, x):
        super(Bunker, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.image = pygame.image.load(r'C:\Users\omarn\Desktop\bunker.png')
        self.rect = self.image.get_rect()
        self.rect.y = self.screen_rect.bottom * 8/10
        self.rect.x = self.screen_rect.right * x / 6 - self.rect.width / 2

    def blitme(self):
        # draw ship at current location
        self.screen.blit(self.image, self.rect)