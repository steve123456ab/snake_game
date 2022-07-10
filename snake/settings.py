'''
    游戏设置
'''
class Settings():
    def __init__(self):
        self.screen_width = 640
        self.screen_height = 480
        self.screen_caption = 'Snake'
        self.bg_color = (255,255,255)
        self.fps = 20
        self.is_food = False
        self.snake_dir = 'right'
        self.is_add_score = False
        self.add_score = 10
