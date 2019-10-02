import pygame
from pygame.sprite import Sprite

class Dead(Sprite):
    def __init__(self, screen, rect):
        super(Dead, self).__init__()
        self.screen = screen
        # Load alien image 
        self.image = pygame.image.load(r'C:\Users\omarn\Desktop\alienexplode.png')
        self.rect = self.image.get_rect()
        self.rect.center = rect.center
        self.image_speed = 15
        self.expectancy = True

    def blitme(self):
        # draw alien at current location
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.image_speed -= 1
        if self.image_speed == 0:
            self.expectancy = False