import pygame
from pygame.sprite import Sprite

def load_image(name):
    image = pygame.image.load(name)
    return image

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start new ships at bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
        # Death.
        self.index = 0
        self.images = []
        self.images.append(load_image('images/shipexplode1.png'))
        self.images.append(load_image('images/shipexplode2.png'))
        self.deadc = 10
        self.dead = False
        self.image_speed = 1

    def update(self, audio):
        if self.dead:
            if not audio.exploa.get_busy():
                self.ai_settings.audio_level = 0
                audio.exploa.play(audio.explob)
            self.image_speed -= 1
            if self.image_speed == 0:
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
                self.image_speed = 30
                self.deadc -= 1
        else:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor
            if self.moving_left and self.rect.left > 0:
                self.center -= self.ai_settings.ship_speed_factor
            self.rect.centerx = self.center

    def blitme(self):
        # draw  ship at its current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
