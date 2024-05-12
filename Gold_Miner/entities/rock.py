import pygame
from definitions import rock_image
class Rock:
    def __init__(self,x,y,size,point):
        self.x = x
        self.y = y
        self.size = size #random.choice([25, 50])
        self.rect = None
        self.is_move = False
        self.point = point
        self.is_explosive = False
        self.rock_image = rock_image
    def draw(self,dt,screen):
        scaled_gold = pygame.transform.scale(self.rock_image, (self.size, self.size))
        self.rect = scaled_gold.get_rect(center=(self.x,self.y))
        screen.blit(scaled_gold, self.rect)
    def update(self,x,y):
        self.x = x
        self.y =y
    def __del__(self):
        pass