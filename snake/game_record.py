'''
    游戏记录
'''
import pygame
from function_tools import print_text


class Game_Record():
    def __init__(self,screen,settings):
        self.screen = screen
        self.settings = settings
        self.max_score = 0
        self.scores = 0
        self.temp_score = 0
        self.font_color = (128,128,128)

    def draw_score(self):
        msg = 'SCORE: {}'.format(self.scores)
        font = print_text(30,msg,self.font_color)
        pos = self.screen.get_width() - (font.get_width() + 10),10
        self.screen.blit(font,pos)

        msg = 'MAX_SCORE: {}'.format(self.max_score)
        font = print_text(30,msg,self.font_color)
        self.screen.blit(font,(10,10))

    def update(self):
        if self.scores > self.max_score:
            self.max_score = self.scores

        if self.scores - self.temp_score >= 100:
            self.settings.fps += 1
            self.temp_score = self.scores

        if self.settings.is_add_score:
            self.scores += self.settings.add_score
            self.settings.is_add_score = False


