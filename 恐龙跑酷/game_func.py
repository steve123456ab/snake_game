'''
    游戏逻辑处理
'''
import sys
import random
import pygame
from map import Map
from cloud import Cloud
from cactus import Cactus
import profile as pf
import function_tools as ft
from bird import Bird


#检查事件
def check_event(settings,cloud_group,screen,map,cactus_group,profile,dino,bird_group,game_record,game_status,music,music_profile):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == settings.CLOUD_EVENT_ID and settings.creative:
            create_cloud(cloud_group,screen,settings)
        elif event.type == settings.CACTUS_EVENT_ID and settings.creative:
            create_cactus(screen,settings,map,cactus_group,game_record)
        elif event.type == settings.BIRD_EVENT_ID and settings.creative:
            create_bird(screen,settings,bird_group,game_record)
        elif event.type == settings.PRODUCE_EVENT_ID and settings.creative:
            is_produce_cactus_or_bird(settings,game_record)
        elif event.type == pygame.KEYDOWN:
            check_keyboard_down(event,settings,profile,screen,map,dino,game_status,music,music_profile)
        elif event.type == pygame.KEYUP:
            check_keyboard_up(event,settings,dino,screen)

#键盘按下事件
def check_keyboard_down(event,settings,profile,screen,map,dino,game_status,music,music_profile):
    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
        jump_handle(dino,music,music_profile)

    elif event.key == pygame.K_DOWN:
        pu_handle(dino)

    elif event.key == pygame.K_ESCAPE:
        game_status.pause = True
        settings.creative = False
        game_status.run_game(op='pause')
        settings.creative = True


#键盘松开事件
def check_keyboard_up(event,settings,dino,screen):
    if not dino.jump_icon and not dino.down_icon:
        dino.running_icon = True
        dino.pu_icon = False



# 恐龙跳跃处理
def jump_handle(dino,music,music_profile):
    if not dino.pu_icon and not dino.jump_icon and not dino.down_icon:
        dino.jump_icon = True
        music.play(music_profile['jump'])


#恐龙蹲下
def pu_handle(dino):
    if not dino.jump_icon and not dino.down_icon:
        dino.pu_icon = True
        dino.running_icon = False
        dino.jump_icon = False
        dino.down_icon = False



#生成云朵
def create_cloud(cloud_group,screen,settings):
    if len(cloud_group) < settings.cloud_limit:
        cloud = Cloud(screen,pf.imgs['cloud'],settings)
        cloud_group.add(cloud)


#绘制云朵并移动
def render_cloud(cloud_group):
    for cloud in cloud_group:
        cloud.draw_cloud()
    for cloud in cloud_group:
        cloud.update()


#更新云朵
def update_cloud(cloud_group,screen,settings):
    #create_cloud(cloud_group,screen,settings)
    render_cloud(cloud_group)


#判断应该生成仙人掌还是飞鸟
def is_produce_cactus_or_bird(settings,game_record):
    if game_record.scores > 500:
        produce_rand = random.randint(0,1)
        if produce_rand == 0:
            settings.is_produce = True
        else:
            settings.is_produce = False


#生成仙人掌
def create_cactus(screen,settings,map,cactus_group,game_record):
    if settings.is_produce:
        cactus = Cactus(screen,settings,map,pf.imgs['cactus'])
        cactus_group.add(cactus)



#绘制并移动仙人掌
def render_cactus(screen,settings,cactus_group):
    for cactus in cactus_group:
        cactus.draw_cactus()

    for cactus in cactus_group:
        cactus.update()


#生成飞鸟
def create_bird(screen,settings,bird_group,game_record):
    if not settings.is_produce:
        bird = Bird(screen,pf.imgs['bird'],settings)
        bird_group.add(bird)


#更新飞鸟
def update_bird(bird_group):
    for bird in bird_group:
        bird.draw_bird()
    for bird in bird_group:
        bird.update()



#更新仙人掌
def update_cactus(cactus_group,screen,settings):
    render_cactus(screen,settings,cactus_group)



#更新恐龙
def update_dino(dino,settings,profile,map,max_point,min_point,music,music_profile):
    dino.draw_dino()
    dino.update(settings,max_point,min_point)
    dino.jump(settings,max_point,min_point,music,music_profile)
    dino.down(settings,min_point)

#更新游戏记录
def update_game_record(game_record,settings,music,music_profile):
    game_record.draw_font()
    game_record.update(music,music_profile)



#更新游戏背景
def update_map(map):
    #map = Map(screen,img_path,settings)
    map.draw_map()
    map.update()


#游戏结束
def is_game_over(dino,cloud_group,cactus_group,game_record,bird_group,game_status,settings,profile,map,max_point,min_point,music,music_profile):
    for cactus in cactus_group:
        if cactus.rect.collidepoint(dino.x,dino.y):
            dino.dead_icon = True
            game_status.game_over_icon = True

    for bird in bird_group:
        if bird.rect.collidepoint(dino.x,dino.y):
            dino.dead_icon = True
            game_status.game_over_icon = True

    if game_status.game_over_icon:
        music.play(music_profile['fail'])
        settings.creative = False
        game_status.pause = True
        game_status.run_game(op='gameover')
        game_over(game_status,cactus_group,bird_group,game_record,cloud_group,settings)
        dino.dead_icon = False

#游戏结束
def game_over(game_status,cactus_group,bird_group,game_record,cloud_group,settings):
    cactus_group.empty()
    bird_group.empty()
    cloud_group.empty()
    settings.map_move_speed = 0.35
    settings.cloud_move_speed = 0.1
    settings.CLOUD_EVENT_ID = pygame.USEREVENT
    settings.cloud_timer = random.randint(3000, 5000)
    settings.cloud_limit = 3
    settings.CACTUS_EVENT_ID = pygame.USEREVENT + 1
    settings.cactus_move_speed = settings.map_move_speed
    settings.cactus_timer = 2000
    settings.dino_up_speed = 0.9
    settings.dino_down_speed = 1
    settings.game_add_score = 0.01
    settings.hist_vic = 100
    settings.game_max_score = 900000
    settings.BIRD_EVENT_ID = pygame.USEREVENT + 2
    settings.bird_move_speed = 0.8
    settings.bird_timer = settings.cactus_timer
    settings.is_produce = True
    settings.PRODUCE_EVENT_ID = pygame.USEREVENT + 3
    settings.produce_timer = 1000
    game_record.scores = 0
    game_record.temp_score = 0
    game_status.game_over_icon = False
    settings.creative = True


#屏幕更新
def update_screen(screen,settings,map,cloud_group,cactus_group,clock,profile,dino,max_point,min_point,game_record,bird_group,game_status,music,music_profile):
    render_cactus(screen, settings, cactus_group)
    screen.fill(settings.bg_color)
    #更新云朵
    update_cloud(cloud_group,screen,settings)
    #更新地图
    update_map(map)
    # 更新仙人掌
    update_cactus(cactus_group, screen, settings)
    #更新恐龙
    update_dino(dino,settings,profile,map,max_point,min_point,music,music_profile)
    # 是否结束游戏
    is_game_over(dino,cloud_group,cactus_group,game_record,bird_group,game_status,settings,profile,map,max_point,min_point,music,music_profile)
    #更新游戏记录
    update_game_record(game_record, settings,music,music_profile)
    #更新飞鸟
    update_bird(bird_group)
    # 更新事件
    check_event(settings, cloud_group, screen,map,cactus_group,profile,dino,bird_group,game_record,game_status,music,music_profile)
    pygame.display.flip()


