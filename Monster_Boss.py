import pygame
from pygame.locals import *
import Monster

class Monster_Boss(Monster.Monster):
    def __init__(self):
        self.img = pygame.image.load('img/Boss1_1.png')

    def Boss_draw(self,screen,position):
        # print(self.img.get_rect())
        rec = self.img.get_rect()
        screen.blit(self.img,(position[0]-rec.width/2,position[1]-rec.height/2))
        self.position = position

    def Boss_Move(self,screen,person_pos,boss_pos):    #person_pos需要获取人物的当前位置
        # distance = (abs(person_pos[0]-boss_pos[0])**2 +abs(person_pos[1]-boss_pos[1]))**0.5
        x_next = 0
        y_next = 0
        if person_pos[0] != boss_pos[0] and person_pos[1] != boss_pos[1]:
            k = abs(person_pos[1]-boss_pos[1])/abs(person_pos[0]-boss_pos[0])
            # print(k)
            x_next = boss_pos[0]+super().speed
            y_next = ((x_next-person_pos[0])/(boss_pos[0]-person_pos[0]))*(boss_pos[1]-person_pos[1])+person_pos[1]
            next_pos = [x_next,y_next]
            # print(next_pos)
            return next_pos
        else:
            return 0
    def is_beat(self):
        pass


