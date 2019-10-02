import pygame
from pygame.sprite import Sprite

def load_image(name):
    image = pygame.image.load(name)
    return image

class ABullet(Sprite):
    def __init__(self, ai_settings, screen, alien):
        # create bullet object, at the ship position
        super(ABullet, self).__init__()
        self.screen = screen
        self.images = []
        self.images.append(load_image(r'C:\Users\omarn\Desktop\alienbullet.png'))
        self.rect = self.images[0].get_rect()
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom
        self.index = 0
        self.image = self.images[self.index]
        self.image_speed = 30
        # Store decimal for the bullet position
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # move bullet down the screen
        self.y += self.speed_factor/2
        self.rect.y = self.y
        # Change sprite
        self.image_speed -= 1
        if self.image_speed == 0:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.image_speed = 30

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)