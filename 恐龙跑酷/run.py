import pygame
from settings import Settings
import sys
import game_func as gf
import profile as pf
from init_game import Init_game
from music import Music

#游戏初始化
pygame.init()

def run_game():
    settings = Settings()
    music = Music()
    profile = pf.imgs
    music_profile = pf.musics
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption(settings.screen_caption)
    running = True
    init_game = Init_game(screen,profile,settings)
    while running:
        arg_ls = [screen,settings,init_game.map,init_game.cloud_group,init_game.cactus_group,
                  init_game.clock,profile,init_game.dino,init_game.max_point,init_game.min_point,init_game.game_record,
                  init_game.bird_group,init_game.game_status,music,music_profile]
        gf.update_screen(*arg_ls)
        settings.creative = False
        init_game.game_status.run_game('start')
        settings.creative = True

if __name__ == '__main__':
    run_game()







