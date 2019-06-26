import pygame
from pygame.locals import *

class Window():
    def __init__(self):     #窗口的初始化
        self.screen = pygame.display.set_mode((800,600))
        self.title = pygame.display.set_caption("打怪兽游戏")

    def run(self):     #在里面调用相关的场景，人物和怪兽信息
        while True:
            self.screen.fill([0,0,0])
            for e in pygame.event.get():
                if e.type == QUIT:
                    exit()



# win = Window()
# win.run()
