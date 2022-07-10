'''
    函数工具
'''
import pygame

pygame.font.init()

def print_text(font_size,text,color):
    font = pygame.font.Font(None,font_size)
    font_text = font.render(text,True,color)
    return font_text

def create_button(screen,color,rect,font):
    button = pygame.draw.rect(screen,color,rect)
    pos = button.centerx - font.get_width() / 2,button.centery - font.get_height() / 2
    screen.blit(font,pos)
    return button

