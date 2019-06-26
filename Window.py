import pygame
from pygame.locals import *
from monster_small import monster_small_jin
from Monster_Boss import Monster_Boss
import time
import random
class Window():
    def __init__(self):     #窗口的初始化
        self.screen = pygame.display.set_mode((1280,720))
        self.title = pygame.display.set_caption("打怪兽游戏")


    def run(self):     #在里面调用相关的场景，人物和怪兽信息
        mb = Monster_Boss()
        mb.Boss_draw(screen=self.screen, position=[500, 300])
        pygame.display.flip()
        while True:
            self.screen.fill([255,255,255])
            print("1111")
            # mb.Boss_draw(screen=self.screen, position=[500, 300])
            # for x,y in random(0,1000):
            #     per = [x,y]
            pygame.draw.circle(self.screen, [255,0,0], [1000,700], 10, 5)
            pos = mb.Boss_Move(screen=self.screen,person_pos=[1000,700],boss_pos=mb.position)
            if pos != 0:
                mb.Boss_draw(screen=self.screen, position=pos)
            pygame.display.update()
            time.sleep(0.1)
            for e in pygame.event.get():
                if e.type == QUIT:
                    exit()



win = Window()
win.run()
