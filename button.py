import pygame.font

class Button:
    def __init__(self, screen, msg, y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.msg = msg
        self.active = False
        self.font = pygame.font.SysFont(None, 48)
        self.width, self.height = self.font.size(self.msg)
        self.button_color = (0, 0, 0)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.screen_rect.centerx, self.screen_rect.bottom * y)
        self.msg_image = self.font.render(self.msg, True, (0, 0, 0), self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
    def prep_msg(self):
        if self.active:
            text_color = (0, 255, 0)
        else:
            text_color = (255, 255, 255)
        self.msg_image = self.font.render(self.msg, True, text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.prep_msg()
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)