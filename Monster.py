import pygame
from pygame.locals import *

class Monster():
    speed = 5
    def __init__(self):
        self.blood = 500    #怪物血量
        # self.img    #怪物贴图
        self.speed = 5
        self.position = []

    def monster_walk(self):     #控制怪物移动
        pass

    def monster_skill(self):        #怪物攻击的技能
        pass

    def monster_appear(self):       #控制怪物出现
        pass

