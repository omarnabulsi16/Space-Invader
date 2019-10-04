import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scorebord
from button import Button
from ship import Ship
from redalien import RAlien
from menu import Menu
from audio import Audio
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(screen, "Play", 80/100)
    score_button = Button(screen, "High Scores", 90/100)
    audio = Audio()
    menu = Menu()
    stats = GameStats(ai_settings)
    sb = Scorebord(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    ralien = RAlien(ai_settings, screen)
    bullets = Group()
    abullets = Group()
    aliens = Group()
    death = Group()
    bunkers = Group()
    gf.create_fleet(ai_settings, screen, aliens)
    while True:
        pygame.time.Clock().tick(ai_settings.game_speed)
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets,
                        score_button, menu, audio, bunkers)
        if stats.game_active:
            ship.update(audio)
            ralien.update(audio)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets,
                              abullets, ralien, audio, death, bunkers)
            gf.update_aliens(ai_settings, screen, ship, aliens, abullets, bunkers)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button,
                         score_button, abullets, menu, ralien, audio, death, bunkers)
run_game()