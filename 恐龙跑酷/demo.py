import pygame
import sys
from PIL import Image
import time

print(pygame.USEREVENT)
print(pygame.USEREVENT + 1)

def get_map_size(img_path):
    image = Image.open(img_path)
    return image.size

pygame.init()

map_size = get_map_size('images/map.png')


def run_game():
    screen = pygame.display.set_mode((map_size[0],400))
    pygame.display.set_caption('demo')
    img_1 = pygame.image.load('images/map.png')
    img_2 = pygame.image.load('images/map.png')
    img_1_width = img_1.get_width()
    img_2_width = img_2.get_width()
    img_1_height = img_1.get_height()
    img_2_height = img_2.get_height()
    gameover_img = pygame.image.load('images/gameover.png')
    restart_img = pygame.image.load('images/restart.png')
    gameover_rect = gameover_img.get_rect()
    restart_rect = restart_img.get_rect()


    x1 = 0
    y1 = screen.get_height() - (img_1_height * 2)
    x2 = img_2_width
    y2 = screen.get_height() - (img_2_height * 2)


    running = True
    max_score = 110
    score = 0
    temp_score = 0
    #screen.fill((230,230,230))
    while running:
        screen.fill((230,230,230))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(img_1,(x1,y1))
        x1 -= 0.3
        screen.blit(img_2,(x2,y2))
        x2 -= 0.3
        if x1 < -img_1_width:
            x1 = x2 + img_2_width
        if x2 < -img_2_width:
            x2 = x1 + img_1_width
        font = pygame.font.Font(None,30)

        if score - temp_score >= 100:
            temp_score = score
            score += temp_score // 1000
            #print(score)
        else:
            score += 0.01

        if score > max_score:
            max_score = score
        #print(temp_score)
        # font = font.render('HI  {}   {}'.format(str(int(max_score)).zfill(6),str(int(score)).zfill(6)),True,(128,128,128))
        # screen.blit(font,(screen.get_width() - (font.get_width() + 10),10))
        screen_center = screen.get_rect().centery
        gameover_pos = screen.get_rect().centerx - gameover_rect.width / 2,screen.get_rect().centery - gameover_rect.height / 2 - 30
        restart_pos = screen.get_rect().centerx - restart_rect.width / 2,screen.get_rect().centery - restart_rect.height / 2 + 30
        screen.blit(gameover_img,gameover_pos)
        screen.blit(restart_img,restart_pos)




        #pygame.time.delay(1)
        pygame.display.update()


if __name__ == '__main__':
    run_game()







