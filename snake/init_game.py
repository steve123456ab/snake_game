import pygame
from snake import Snake
from game_record import Game_Record
from game_status import Game_Status

class Init_Game():
    def __init__(self,screen,settings):
        self.food_group = []
        self.snake = Snake(screen, settings)
        self.game_record = Game_Record(screen, settings)
        self.clock = pygame.time.Clock()
        self.game_record = Game_Record(screen,settings)
        self.game_status = Game_Status(screen,settings)