'''
    游戏配置项
'''
import random
from function_tools import *
import pygame


class Settings():
    def __init__(self):
        self.screen_settings()
        self.map_settings()
        self.cloud_settings()
        self.cactus_settings()
        self.dino_settings()
        self.game_record()
        self.bird_settings()
        self.other_settings()

    def screen_settings(self):
        self.screen_width = get_map_size('images/map.png')[0]
        self.screen_height = 350
        self.screen_caption = 'Dinosaur Parkour'
        self.bg_color = (255, 255, 255)

    def map_settings(self):
        self.map_move_speed = 0.35

    def cloud_settings(self):
        self.cloud_move_speed = 0.1
        self.CLOUD_EVENT_ID = pygame.USEREVENT
        self.cloud_timer = random.randint(3000, 5000)
        self.cloud_limit = 3

    def cactus_settings(self):
        self.CACTUS_EVENT_ID = pygame.USEREVENT + 1
        self.cactus_move_speed = self.map_move_speed
        self.cactus_timer = 2000

    def dino_settings(self):
        self.dino_up_speed = 0.9
        self.dino_down_speed = 1

    def game_record(self):
        self.game_add_score = 0.01
        self.hist_vic = 100
        self.game_max_score = 900000

    def bird_settings(self):
        self.BIRD_EVENT_ID = pygame.USEREVENT + 2
        self.bird_move_speed = 0.8
        self.bird_timer = self.cactus_timer

    def other_settings(self):
        self.is_produce = True
        self.PRODUCE_EVENT_ID = pygame.USEREVENT + 3
        self.produce_timer = 1000
        self.creative = True

