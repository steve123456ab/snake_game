'''
    游戏状态
'''
import pygame
import sys
from function_tools import create_button

class Game_Status():
    def __init__(self, screen, start_image,pause_img,gameover_img,restart_img):
        self.screen = screen
        self.pause = True
        self.start_img = pygame.image.load(start_image)
        self.pause_img = pygame.image.load(pause_img)
        self.gameover_img = pygame.image.load(gameover_img)
        self.restart_img = pygame.image.load(restart_img)
        self.game_over_icon = False

    def start_game(self,event):
        self.pause = True
        button_info = create_button(self.screen,'START')
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_info.collidepoint(mouse_pos):
                self.pause = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.pause = False



    def pause_game(self,event):
        self.pause = True
        pos = self.screen.get_rect().centerx - self.pause_img.get_width() / 2,self.screen.get_rect().centery - self.pause_img.get_height() / 2
        self.screen.blit(self.pause_img,pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.pause = False


    def gameover(self,event):
        gameover_rect = self.gameover_img.get_rect()
        restart_rect = self.restart_img.get_rect()
        gameover_pos = self.screen.get_rect().centerx - gameover_rect.width / 2, self.screen.get_rect().centery - gameover_rect.height / 2 - 30
        restart_pos = self.screen.get_rect().centerx - restart_rect.width / 2, self.screen.get_rect().centery - restart_rect.height / 2 + 30
        self.screen.blit(self.gameover_img, gameover_pos)
        self.screen.blit(self.restart_img, restart_pos)
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.screen.get_rect().collidepoint(mouse_pos):
                self.pause = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_RETURN:
                self.pause = False
            if event.key == pygame.K_SPACE:
                self.pause = False


    def run_game(self,op):
        while self.pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if op == 'start':
                    self.start_game(event)
                elif op == 'pause':
                    self.pause_game(event)
                elif op == 'gameover':
                    self.gameover(event)

            pygame.display.update()



