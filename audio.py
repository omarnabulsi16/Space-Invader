import pygame

class Audio:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(5)
        self.exploa = pygame.mixer.Channel(2)
        self.explob = pygame.mixer.Sound(r"C:\Users\omarn\Desktop\explosion.wav")
        self.omin = pygame.mixer.Channel(0)
        self.omina = pygame.mixer.Sound(r"C:\Users\omarn\Desktop\bk1.wav")
        self.ominb = pygame.mixer.Sound(r"C:\Users\omarn\Desktop\bk2.wav")
        self.ominc = pygame.mixer.Sound(r"C:\Users\omarn\Desktop\bk3.wav")
        self.omind = pygame.mixer.Sound(r"C:\Users\omarn\Desktop\bk4.wav")
    @staticmethod
    def play():
        # background music
        pygame.mixer_music.set_volume(.5)
        pygame.mixer.music.play()