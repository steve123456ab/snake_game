'''
    其他工具
'''
from PIL import Image
import pygame

def get_map_size(image_path):
    img = Image.open(image_path)
    return img.size


#获取最高的仙人掌图片
def get_max_cactus_height(images_path):
    max = 0
    for img_path in images_path:
        img = Image.open(img_path)
        if img.size[1] >= max:
            max = img.size[1]
    return max

#获得最低的仙人掌图片
def get_min_cactus_low(images_path):
    min = Image.open(images_path[0]).size[1]
    for img_path in images_path:
        img = Image.open(img_path)
        if img.size[1] <= min:
            min = img.size[1]
    return min


#获取恐龙跳跃的最高点和最低点
def get_max_min_point(pf,screen,map):
    max = get_max_cactus_height(pf['cactus'])
    min = get_min_cactus_low(pf['cactus'])
    max_point = screen.get_height() - ((max * 3))
    min_point = screen.get_height() - (map.height * 4)
    return max_point,min_point

#screen.get_height() - ((max * 3))
#screen.get_height() - (map.height * 4)
#pygame写文字方法
def print_text(font_size,text,color):
    font = pygame.font.Font(None,font_size)
    font = font.render(text,True,color)
    return font


#绘制一个按钮
def create_button(screen,text):
    position = screen.get_rect().centerx - 200 / 2,screen.get_rect().centery - 50 / 2,200,50
    button = pygame.draw.rect(screen,(128,128,128),position,0)
    font = print_text(30,text,(255,255,255))
    screen.blit(font,(button.centerx - font.get_width() / 2,button.centery - font.get_height() / 2))
    return button





