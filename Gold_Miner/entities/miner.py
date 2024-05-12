from definitions import miner_images
class Miner:
    def __init__(self, pos_x, pos_y, speed):
        '''
        swinging = 0 | expanding = 1 | retracting = 2 | yeah = 3 | TNT = 4
        '''
        self.images = miner_images
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.current_frame = 0
        self.state = 0
        self.is_play_done = False
        self.list_frame = [0,1,2]
    def draw(self, screen):
        image = self.images[self.list_frame[int(self.current_frame)]]
        screen.blit(image, (self.pos_x, self.pos_y))
    def update(self, dt):
        match self.state:
            case 4: #TNT
                # print("use TNT")
                self.list_frame = [3,4,5]
                self.animation(dt)
            case 3: #Strength
                self.list_frame = [6,7]
                self.animation(dt)
            case 2: #retracting
                self.list_frame = [2,1,0]
                self.animation(dt)
            case 1: #expanding
                self.list_frame = [2]
                self.animation(dt)
            case 0: # swinging
                self.list_frame = [0]
                self.animation(dt)
    def animation(self,dt):
        if self.is_play_done:
            self.state = 0
            self.is_play_done = False
        self.current_frame += self.speed * dt
        if self.current_frame >= len(self.list_frame) :
            self.current_frame = 0
            if (self.state == 3 or self.state == 4):
                self.state = 0
                self.is_play_done = True