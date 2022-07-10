'''
    蛇类
'''
import pygame
import copy

class Snake(pygame.sprite.Sprite):
    def __init__(self,screen,settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.head = [80,20]
        self.body = [[80,20],[60,20],[40,20],[20,20]]
        self.foot = [20,20]
        self.width = 20
        self.height = 20
        self.color = (0,255,0)
        self.is_dead = False


    def draw_snake(self):
        for body in self.body:
            pygame.draw.rect(self.screen,self.color,(body[0],body[1],self.width,self.height),0)


    def update(self):
        if self.settings.snake_dir == 'left' and self.settings.snake_dir != 'right':
            self.head[0] -= 20
        elif self.settings.snake_dir == 'right' and self.settings.snake_dir != 'left':
            self.head[0] += 20
        elif self.settings.snake_dir == 'up' and self.settings.snake_dir != 'down':
            self.head[1] -= 20
        elif self.settings.snake_dir == 'down' and self.settings.snake_dir != 'up':
            self.head[1] += 20
        self.body.insert(0,copy.deepcopy(self.head))


    def eat(self,food_group):
        if food_group:
            if food_group[0].x == self.head[0] and food_group[0].y == self.head[1]:
                food_group.clear()
                self.settings.is_food = False
                self.add_body()
                self.settings.is_add_score = True
        self.body.pop()

    def add_body(self):
        if self.settings.snake_dir == 'left':
            self.foot[0] -= 20
        elif self.settings.snake_dir == 'right':
            self.foot[0] += 20
        elif self.settings.snake_dir == 'up':
            self.foot[1] -= 20
        elif self.settings.snake_dir == 'down':
            self.foot[1] += 20
        self.body.append(copy.deepcopy(self.foot))


    def dead(self):
        if self.body[0][0] < 0 or self.body[0][0] > self.settings.screen_width:
            self.is_dead = True
            return
        if self.body[0][1] < 0 or self.body[0][1] > self.settings.screen_height:
            self.is_dead = True
            return
        for body in self.body[1:]:
            if self.head[0] == body[0] and self.head[1] == body[1]:
                self.is_dead = True
                return











