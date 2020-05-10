import pygame
import sys

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
import game_function as gf


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )
    pygame.display.set_caption("Game")
    ship = Ship(game_settings, screen)
    bullets = Group()

    alien = Alien(game_settings, screen)

    while True:
        gf.chek_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, ship, alien, bullets)



run_game()
