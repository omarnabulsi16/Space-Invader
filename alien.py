import pygame
import random
from pygame.sprite import Sprite
from alienbullet import ABullet

def load_image(name):
    image = pygame.image.load(name)
    return image

class Alien(Sprite):
    def __init__(self, ai_settings, screen, row_number, alien_number):
        # initialize the alien and set starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load aliens 
        if 0 <= row_number <= 1:
            self.images = []
            self.images.append(load_image('images/bluealien1.png'))
            self.images.append(load_image('images/bluealien2.png'))
            self.worth = 10
        elif 2 <= row_number <= 3:
            self.images = []
            self.images.append(load_image('images/purplealien1.png'))
            self.images.append(load_image('images/purplealien2.png'))
            self.worth = 20
        elif 4 <= row_number <= 5:
            self.images = []
            self.images.append(load_image('images/greenalien1.png'))
            self.images.append(load_image('images/greenalien2.png'))
            self.worth = 40
        if alien_number % 2 == 0:
            self.index = 0
        else:
            self.index = 1
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.image_speed = 30
        # Start new aliens in the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store alien position
        self.x = float(self.rect.x)
        
    def blitme(self):
        # Draw alien at current location
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self, ai_settings, screen, abullets):
        self.image_speed -= 1
        if self.image_speed == 0:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.image_speed = 30
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        # Randomly shoot alien bullets
        if random.randint(0, 2000) == 0:
            new_bullet = ABullet(ai_settings, screen, self)
            abullets.add(new_bullet)
