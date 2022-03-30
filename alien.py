import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        # initialize the alien and set its atrt position
        super().__init__()
        self.screen = ai_game.screen

        # load the ailen image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.recy.y = self.rect.height

        # store the aliens exact horizontal position
        self.x = float(self.rect.x)
