'''
    云朵类
'''
import pygame
import random


class Cloud(pygame.sprite.Sprite):
    def __init__(self,screen,img_path,settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.x = self.screen.get_width() + self.width
        self.y = random.randint(self.height,self.screen.get_height() // 2)


    def draw_cloud(self):
        self.screen.blit(self.image,(self.x,self.y))

    def update(self):
        self.x -= self.settings.cloud_move_speed
        if self.x < -self.width:
            self.kill()








