'''
    游戏逻辑
'''
import pygame
from food import Food
import sys


def check_event(settings,game_status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_event_down(event,settings,game_status)
        elif event.type == pygame.KEYUP:
            check_event_up()


def check_event_down(event,settings,game_status):
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        if settings.snake_dir != 'down':
            settings.snake_dir = 'up'
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        if settings.snake_dir != 'up':
            settings.snake_dir = 'down'
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        if settings.snake_dir != 'right':
            settings.snake_dir = 'left'
    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        if settings.snake_dir != 'left':
            settings.snake_dir = 'right'
    elif event.key == pygame.K_ESCAPE:
        game_status.pause = True
        game_status.run(op='pause')




def check_event_up():
    pass


def update_food(settings,screen,food_group):
    if not settings.is_food:
        food = Food(screen,settings)
        food_group.append(food)
        settings.is_food = True

    for food in food_group:
        food.draw_food()


#游戏重置
def game_reset(snake,game_record,settings,food_group):
    snake.is_dead = False
    game_record.scores = 0
    game_record.temp_score = 0
    settings.fps = 20
    snake.head = [80, 20]
    snake.body = [[80, 20], [60, 20], [40, 20], [20, 20]]
    snake.foot = [20, 20]
    food_group.clear()
    settings.is_food = False
    settings.snake_dir = 'right'


def is_game_over(snake,game_status,game_record,settings,food_group):
    if snake.is_dead:
        game_status.pause = True
        game_status.run(op='game_over')
        game_reset(snake,game_record,settings,food_group)


#更新蛇
def update_snake(snake,food_group,game_status,game_record,settings):
    snake.draw_snake()
    snake.eat(food_group)
    snake.update()
    snake.dead()



#更新分数
def update_score(game_record):
    game_record.draw_score()
    game_record.update()



def update_screen(clock,settings,screen,food_group,snake,game_record,game_status):
    screen.fill(settings.bg_color)
    update_food(settings,screen,food_group)
    update_snake(snake, food_group, game_status, game_record, settings)
    update_score(game_record)
    check_event(settings, game_status)
    is_game_over(snake,game_status,game_record,settings,food_group)
    pygame.display.update()
    clock.tick(settings.fps)

