'''
    食物类
'''
import pygame
import random


class Food(pygame.sprite.Sprite):
    def __init__(self, screen,settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.color = (255,0,0)
        self.width = 20
        self.height = 20
        self.x = random.randrange(0,self.settings.screen_width - self.width,self.width)
        self.y = random.randrange(0,self.settings.screen_height - self.height,self.width)

    def draw_food(self):
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.height),0)











