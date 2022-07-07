'''
    游戏记录
'''
import pygame
from function_tools import print_text

class Game_Record():
    def __init__(self, screen,settings):
        self.screen = screen
        self.settings = settings
        self.max_score = 0
        self.temp_score = 0
        self.scores = 0

    def draw_font(self):
        text = 'HI  {}   {}'.format(str(int(self.max_score)).zfill(6),str(int(self.scores)).zfill(6))
        font_info = print_text(30,text,(128,128,128))
        self.screen.blit(font_info,(self.screen.get_width() - (font_info.get_width() + 10),10))


    def update(self,music,music_profile):
        if self.scores - self.temp_score >= self.settings.hist_vic:
            music.play(music_profile['up'])
            self.temp_score = self.scores
            self.scores += self.temp_score / (self.settings.hist_vic * 1)
            self.settings.map_move_speed += 0.03
            self.settings.cactus_move_speed += 0.03
            self.settings.bird_move_speed += 0.01
            if self.scores >= self.settings.game_max_score:
                music.play(music_profile['finish'])
                self.scores = 0
        else:
            self.scores += self.settings.game_add_score

        if self.scores > self.max_score:
            self.max_score = self.scores






