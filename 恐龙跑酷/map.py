'''
    游戏地图类
'''
import pygame


class Map(pygame.sprite.Sprite):
    def __init__(self, screen, img_path, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.x1 = 0
        self.y1 = self.screen.get_height() - (self.rect.height)
        self.x2 = self.rect.width
        self.y2 = self.y1

    def draw_map(self):
        self.screen.blit(self.image,(self.x1,self.y1))
        self.screen.blit(self.image,(self.x2,self.y2))

    def update(self):
        self.x1 -= self.settings.map_move_speed
        self.x2 -= self.settings.map_move_speed
        if self.x1 < -self.width:
            self.x1 = self.x2 + self.width
        if self.x2 < -self.width:
            self.x2 = self.x1 + self.width








