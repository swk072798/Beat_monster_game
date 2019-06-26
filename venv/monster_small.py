import pygame
from pygame.locals import *
import Monster

class monster_small_jin(Monster.Monster):
    def __init__(self):
        self.img = pygame.image.load('img/ghost.jpg')
        self.size = [5,10]


    def monster_draw(self,screen,position,size):
        # rect = self.img.get_rec()
        # rect.left
        screen.blit(self.img,(position[0],position[1],size[0],size[1]))
        self.position = position

    def monster_walk(self,person_pos):
        
        
        pass
