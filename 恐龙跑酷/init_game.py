'''
    初始游戏
'''
import pygame
from dino import Dino
from map import Map
from pygame.sprite import Group
from cloud import Cloud
import function_tools as ft
from game_record import Game_Record
from game_status import Game_Status


class Init_game():
    def __init__(self,screen,profile,settings):
        self.cloud_group = Group()
        self.cactus_group = Group()
        self.bird_group = Group()
        self.map = Map(screen, profile['map'], settings)
        self.dino = Dino(screen,profile['dino'],profile['dead'],self.map)
        pygame.time.set_timer(settings.CLOUD_EVENT_ID, settings.cloud_timer)
        pygame.time.set_timer(settings.CACTUS_EVENT_ID, settings.cactus_timer)
        pygame.time.set_timer(settings.BIRD_EVENT_ID,settings.bird_timer)
        pygame.time.set_timer(settings.PRODUCE_EVENT_ID,settings.produce_timer)
        self.clock = pygame.time.Clock()
        self.max_point,self.min_point = ft.get_max_min_point(profile, screen, self.map)
        self.game_record = Game_Record(screen,settings)
        args = [profile['start_button'],profile['pause'],profile['game_over'],profile['restart']]
        self.game_status = Game_Status(screen,*args)

