import pygame
import sys
from function_tools import print_text

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Snake')
screen.fill((255,255,255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        game_over_font = print_text(60, 'GAME  OVER', (255, 0, 0))
        try_again_font = print_text(30, 'Enter space or mouse try again...', (0, 255, 0))
        center = screen.get_rect().centerx, screen.get_rect().centery
        font_pos_y = center[1] - 50, center[1] + 40
        font_pos_x = center[0] - game_over_font.get_width() / 2, center[0] - try_again_font.get_width() / 2
        screen.blit(game_over_font, (font_pos_x[0], font_pos_y[0]))
        screen.blit(try_again_font, (font_pos_x[1], font_pos_y[1]))



    pygame.display.update()




