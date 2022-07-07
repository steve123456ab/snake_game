'''
    玩家恐龙类
'''
import pygame
from function_tools import get_max_min_point

class Dino(pygame.sprite.Sprite):
    def __init__(self,screen,images,dead_img,map):
        super().__init__()
        self.screen = screen
        self.map = map
        self.images = images
        self.dead_img = dead_img
        self.add_img()
        self.img_index = 0
        self.image = self.images[self.img_index]
        self.rect = self.image.get_rect()
        self.running_icon = True
        self.pu_icon = False
        self.jump_icon = False
        self.down_icon = False
        self.dead_icon = False
        self.load_img_info()
        self.x = self.rect.width - 10
        self.y = self.screen.get_height() - self.rect.height


    def add_img(self):
        images = []
        for img in self.images:
            images.append(pygame.image.load(img))
        images.append(self.dead_img)
        self.images = images

    def load_img_info(self):
        self.image = self.images[self.img_index]
        self.rect = self.image.get_rect()


    def draw_dino(self):
        self.screen.blit(self.images[self.img_index],(self.x,self.y))


    def update(self,settings,max_point,min_point):
        if self.running_icon:
            if self.img_index == 0:
                self.img_index = 1
            else:
                self.img_index = 0
            self.load_img_info()
            if not self.jump_icon and not self.down_icon:
                self.y = self.screen.get_height() - self.rect.height

        if self.pu_icon:
            if self.img_index == 2:
                self.img_index = 3
            else:
                self.img_index = 2
            self.load_img_info()
            self.y = self.screen.get_height() - self.rect.height

        if self.dead_icon:
            self.img_index = 4
            self.load_img_info()
            self.y = self.screen.get_height() - self.rect.height


    def jump(self,settings,max_point,min_point,music,music_profile):
        if self.jump_icon:
            #music.play(music_profile['jump'])
            self.y -= settings.dino_up_speed
            if self.y <= max_point:
                self.down_icon = True
                self.jump_icon = False


    def down(self,settings,min_point):
        if self.down_icon:
            self.y += settings.dino_down_speed
            if self.y >= min_point:
                self.down_icon = False









