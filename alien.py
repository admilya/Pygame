import pygame

from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, game_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load('/home/user/Desktop/game/alien.bmp')
        self.rect = self.image.get_rect()

        # poloshenie alien
        self.rect.x += 1665
        self.rect.y += 0
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

