import pygame
from definitions import gold_image
class Gold:
    def __init__(self,x,y,size,point):
        self.x = x
        self.y = y
        self.size = size
        # self.size = random.choice([30,70,90,150])
        self.rect = None
        self.is_move = False
        self.point = point
        self.is_explosive = False
        self.gold_image = gold_image
    def draw(self,dt,screen):
        scaled_gold = pygame.transform.scale(self.gold_image, (self.size, self.size))
        self.rect = scaled_gold.get_rect(center=(self.x,self.y))
        screen.blit(scaled_gold, self.rect)
    def update(self,x,y):
        self.x = x
        self.y =y
    def __del__(self):
        pass