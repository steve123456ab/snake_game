'''
    飞鸟类
'''
import pygame
import random

class Bird(pygame.sprite.Sprite):
    def __init__(self, screen, images, settings):
        super().__init__()
        self.img_index = 0
        self.screen = screen
        self.settings = settings
        self.images = images
        self.add_img_info()
        self.image = self.images[self.img_index]
        self.get_img_info()


    def add_img_info(self):
        img_ls = []
        for img in self.images:
            img_ls.append(pygame.image.load(img))
        self.images = img_ls

    def get_img_info(self):
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.x = self.screen.get_width() + self.width
        self.y = random.randint(self.width, self.screen.get_height() - (self.height))


    def draw_bird(self):
        self.screen.blit(self.image,(self.x,self.y))

    def update(self):
        self.x -= self.settings.bird_move_speed
        if self.x < -self.width:
            self.kill()
        self.img_index += 1
        self.image = self.images[self.img_index % 2]



