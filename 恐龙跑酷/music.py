'''
    游戏音乐
'''
import pygame

pygame.mixer.init()

class Music():
    def __init__(self):
        self.volumn = 0.5

    def play(self,name):
        pygame.mixer.music.load(name)
        pygame.mixer.music.set_volume(self.volumn)
        pygame.mixer.music.play()
