import pygame
from settings import Settings
import sys
import game_func as gf
from init_game import Init_Game
from game_status import Game_Status

def run_game():
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption(settings.screen_caption)
    running = True
    init_game = Init_Game(screen,settings)
    while running:
        args = [init_game.clock,settings,screen,init_game.food_group,init_game.snake,
                init_game.game_record,init_game.game_status]
        gf.update_screen(*args)
        init_game.game_status.run('start')



if __name__ == '__main__':
    run_game()






