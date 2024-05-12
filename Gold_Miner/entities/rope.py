from definitions import *
from scenes.util import load_sound
from entities.hook import Hook
class Rope:
    def __init__(self, x1, y1, speed,hoo_images,tnt=0,buffspeed=1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1
        self.y2 = y1
        self.length = 50
        self.speed = speed
        self.buff_speed = buffspeed
        self.weight = 1
        self.speed_swinging = 50
        self.direction = 90
        self.state = 'swinging'
        self.hook_images = hook_images
        self.hook_image = 0
        self.hook = Hook(self.x2, self.y2)
        self.item = None
        self.is_taking = False
        self.have_TNT = tnt
        self.is_use_TNT = False
        self.timer = -1
        self.text = ""
        self.x_text = 650
        self.y_text = 0
        self.text_size =0
        self.time_text = 0
        self.text_direction = "None"
    def draw(self, screen):
        pygame.draw.line(screen, (51, 51, 51), (self.x1, self.y1), (self.x2, self.y2), 3)
        self.hook.draw(screen)
    def update(self, miner, dt,screen):
        if self.timer <= 0:
            if self.state == 'swinging':
                # print(self.x2,self.y2,self.length,self.direction)
                self.direction += self.speed_swinging * dt
                if self.y2 < 54 or self.direction < 14 or self.direction > 166: #fix ket
                    self.y2 = self.y1 + 50
                    self.length = 50
                    self.direction = 90
                if self.direction > 165 or self.direction < 15:
                    self.speed_swinging = -self.speed_swinging
                self.x2 = self.x1 + self.length * math.cos(math.radians(self.direction))
                self.y2 = self.y1 + self.length * math.sin(math.radians(self.direction))

                if miner.state == 1:
                    self.state = 'expanding'
            elif self.state == 'expanding':
                # pygame.mixer.stop()
                # grab_start_sound.play()
                load_sound("grab_start_sound")
                self.length += self.speed * dt * 1.5
                self.x2 = self.x1 + self.length * math.cos(math.radians(self.direction))
                self.y2 = self.y1 + self.length * math.sin(math.radians(self.direction))

                if self.x2 <= 0 or self.x2 >= screen_width or self.y2 <= 0 or self.y2 >= screen_height:
                    self.state = 'retracting'
            elif self.state == 'retracting':
                # pygame.mixer.stop()
                # grab_back_sound.play()
                load_sound("grab_back_sound")
                self.length -= (self.speed * dt * self.buff_speed) / self.weight
                self.x2 = self.x1 + self.length * math.cos(math.radians(self.direction))
                self.y2 = self.y1 + self.length * math.sin(math.radians(self.direction))
                if(self.item != None): # nếu đụng trúng vật phẩm
                    self.weight = int(self.item.size/30)
                    self.item.draw(dt,screen)
                    if (self.direction < 90):
                        new_x2 = self.x2
                    else:
                        new_x2 = self.x2 - int(self.item.size/5)
                    self.item.update(new_x2 ,self.y2 + int(self.item.size/2.2))
                    self.hook_image = 1 # hinh anh keo vật phẩm
                else:
                    self.hook_image = 2 # hinh anh keo k co gì
                if self.length <= 50:
                    if self.item != None :
                        if self.item.point > 0 and self.is_use_TNT == False:
                            score = get_score()
                            score += self.item.point
                            set_score(score)
                            self.text = str(self.item.point)
                            self.x_text = 650
                            self.text_size =0
                            self.time_text = 0
                            self.text_direction = "left"
                        else:
                            if self.item.point == -1 and self.is_use_TNT == False: #dynamite
                                self.text = "dynamite"
                                self.text_direction = "left"
                                self.x_text = 650
                                self.text_size =0
                                self.time_text = 0
                                self.have_TNT +=1
                            elif self.item.point == -2 and self.is_use_TNT == False:
                                self.text = "strength"
                                self.text_direction = "left"
                                self.x_text = 650
                                self.text_size =0
                                self.time_text = 0
                                self.buff_speed = 2 #strength
                        self.timer = 200
                        del self.item
                        self.item = None
                        self.speed_swinging = 0
                    self.hook_image = 0
                    self.weight = 1
                    self.state = 'swinging'
                    load_sound("hook_reset_sound")
                    if not(self.is_use_TNT):
                        miner.state = 0
        else:
            self.timer -= self.speed * dt
            self.speed_swinging = 50
        self.hook.update(self.hook_image,self.x2,self.y2,self.direction)