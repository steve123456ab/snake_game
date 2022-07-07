'''
    仙人掌类
'''

import pygame
import random

class Cactus(pygame.sprite.Sprite):
    def __init__(self, screen, settings, map, images):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.images = images
        self.image = pygame.image.load(random.choice(images))
        self.rect = self.image.get_rect()
        self.x = self.screen.get_width() + self.rect.width
        self.y = self.screen.get_height() - (self.rect.height)
        self.width = self.rect.width
        self.height = self.rect.height

    def draw_cactus(self):
        self.screen.blit(self.image,(self.x,self.y))

    def update(self):
        self.x -= self.settings.cactus_move_speed
        if self.x < -self.width:
            self.kill()












