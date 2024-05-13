from definitions import tnt_image,empty
from entities.explosive import Explosive
class TNT:
    def __init__(self,x,y, tnt_image):
        self.x = x
        self.y = y
        self.size = 30
        self.rect = None
        self.is_move = True
        self.image = tnt_image
        self.dt = None
        self.explosive = Explosive(self.x-128, self.y-128, 12)
        self.is_explosive = True
        self.screen = None
        self.point = 0
    def draw(self,dt,screen):
        self.screen = screen
        self.dt = dt
        self.rect = self.image.get_rect(center=(self.x,self.y))
        screen.blit(self.image, self.rect)
    def update(self,x,y):
        if(self.is_move == False):
            self.image = empty
            self.explosive.draw(self.screen)
            self.explosive.update(self.dt)
    def __del__(self):
        pass