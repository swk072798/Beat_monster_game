import pygame
from pygame.locals import *

class Person():
    def __init__(self):   #初始化人物元素
        self.blood = 100  #初始血量100
        self.aggressivity = 5  #攻击力5
        self.speed = 10   #移动速度10
        self.img = pygame.image.load()   #人物贴图
        self.position = [0,200]            #人物初始位置
        pass

    def walk_and_run(self):   #设置移动
        pass

    def release_skills(self):   #释放技能
        pass
