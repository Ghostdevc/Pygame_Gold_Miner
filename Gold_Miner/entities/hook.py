import pygame
from definitions import hook_images
class Hook:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0
        self.images = hook_images
        self.current_frame=0
        self.rect = None
    def draw(self, screen):
        image = self.images[int(self.current_frame)]
        image = pygame.transform.rotate(image,self.direction)
        self.rect = image.get_rect(center= (self.x,self.y))
        screen.blit(image, self.rect)
    def update(self, frame,new_x,new_y,direction):
        self.current_frame = frame
        self.x = new_x
        self.y = new_y
        self.direction = 90 - direction