import pygame


class Ship:

    def __init__(self, game_settings, screen):
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load('/home/user/Desktop/game/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.screen_rect.x
        self.rect.y = self.screen_rect.y

        self.rect.bottom = self.screen_rect.bottom
        self.center = [float(self.rect.x), float(self.rect.y)]

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center[0] += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center[0] -= self.game_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center[1] -= self.game_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center[1] += self.game_settings.ship_speed_factor

        self.rect.x = self.center[0]
        self.rect.y = self.center[1]


    def blitme(self):
        self.screen.blit(self.image, self.rect)