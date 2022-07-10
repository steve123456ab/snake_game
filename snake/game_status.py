'''
    游戏状态
'''
import pygame
import sys
from function_tools import print_text
from function_tools import create_button

pygame.init()

class Game_Status():
    def __init__(self,screen,settings):
        self.screen = screen
        self.settings = settings
        self.pause = True


    def start_game(self,event):
        font = print_text(30,'START',(255,255,255))
        width = 130
        height = 30
        rect = self.screen.get_rect().centerx - width / 2,self.screen.get_rect().centery - height / 2,width,height
        button = create_button(self.screen,(0,255,0),rect,font)
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.pause = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(mouse):
                self.pause = False

    def pause_game(self,event):
        font = print_text(50,'PAUSE',(255,0,0))
        pos = self.screen.get_rect().centerx - font.get_width() / 2,self.screen.get_rect().centery - font.get_height() / 2
        self.screen.blit(font,pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.pause = False

    def game_over(self,event):
        game_over_font = print_text(60,'GAME OVER',(255,0,0))
        try_again_font = print_text(30,'Enter space or mouse try again...',(0,255,0))
        center = self.screen.get_rect().centerx,self.screen.get_rect().centery
        font_pos_y = center[1] - 50,center[1] + 40
        font_pos_x = center[0] - game_over_font.get_width() / 2,center[0] - try_again_font.get_width() / 2
        self.screen.blit(game_over_font,(font_pos_x[0],font_pos_y[0]))
        self.screen.blit(try_again_font,(font_pos_x[1],font_pos_y[1]))
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.pause = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.screen.get_rect().collidepoint(mouse_pos):
                self.pause = False



    def run(self,op):
        while self.pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if op == 'start':
                    self.start_game(event)
                elif op == 'pause':
                    self.pause_game(event)
                elif op == 'game_over':
                    self.game_over(event)

            pygame.display.update()





