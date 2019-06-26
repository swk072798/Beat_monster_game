import pygame
from pygame.locals import *
import Monster

class monster_small_jin(Monster.Monster):
    def __init__(self):
        self.img = pygame.image.load('img/ghost.jpg')

    def monster_walk(self,person_pos):
        pass
