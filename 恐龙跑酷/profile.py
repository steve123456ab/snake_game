'''
    游戏资源
'''
import pygame
import os

imgs = {
    'dino':[os.getcwd() + '\\' + 'images\\dragon_{}.png'.format(i) for i in range(1,6)],
    'cactus':[os.getcwd() + '\\' + 'images\\item_{}.jpeg'.format(i) for i in range(1,9)],
    'bird':[os.getcwd() + '\\' + 'images\\bird_{}.png'.format(i) for i in range(1,3)],
    'cloud':os.getcwd() + '\\' + 'images\\cloud.png',
    'dead':os.getcwd() + '\\' + 'images\\dead.png',
    'game_over':os.getcwd() + '\\' + 'images\\gameover.png',
    'map':os.getcwd() + '\\' + 'images\\map.png',
    'pause':os.getcwd() + '\\' + 'images\\pause.png',
    'restart':os.getcwd() + '\\' + 'images\\restart.png',
    'start_button':os.getcwd() + '\\' + 'images\\start_button.png',
}

musics = {
    'up':os.getcwd() + '\\' + 'music\\升级.mp3',
    'fail':os.getcwd() + '\\' + 'music\\失败.mp3',
    'jump':os.getcwd() + '\\' + 'music\\跳跃.mp3',
    'finish':os.getcwd() + '\\' + 'music\\通关升级.mp3'
}


