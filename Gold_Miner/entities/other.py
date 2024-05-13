class Other:
    def __init__(self,x,y,image,point):
        self.x = x
        self.y = y
        self.size = 30
        self.rect = None
        self.is_move = True
        self.image = image
        self.point = point
        self.is_explosive = False
    def draw(self,dt,screen):
        # global mole_image
        self.rect = self.image.get_rect(center=(self.x,self.y))
        screen.blit(self.image, self.rect)
    def update(self,x,y):
        self.x = x
        self.y =y
    def __del__(self):
        pass