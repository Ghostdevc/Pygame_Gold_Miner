import os

from entities.miner import Miner
from entities.rope import Rope
from entities.explosive import Explosive
from entities.button import Button
from entities.angryman import Shopkeeper
from scenes.scene import Scene
from scenes.util import *
clock = pygame.time.Clock()


class SceneMananger(object):
    def __init__(self):
        self.go_to(StartScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self

class StartScene(object):
    def __init__(self):
        super(StartScene, self).__init__()
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Libre.ttf'), 48)
        self.button = Button(120,20,gold_image,2)
        self.higt_score_btn = Button(80,500,hight_score,1)
    def render(self, screen):
        screen.blit(start_BG,(0,0))
        self.button.render(screen)
        self.higt_score_btn.render(screen)
        screen.blit(miner_menu,miner_menu_rect)
        text = self.font.render('Oyna', True, (255, 255, 255))
        screen.blit(text, (250, 160))
    def update(self,screen):
        pass
    def start(self):
        set_time(pygame.time.get_ticks()/1000)
        self.manager.go_to(GameScene(level=get_level()))
    def handle_events(self, events):
        if self.button.is_click():
            self.start()
        if self.higt_score_btn.is_click():
            self.manager.go_to(HighScoreScene())

class FinishScene(object):
    def __init__(self):
        super(FinishScene, self).__init__()
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Libre.ttf'), 28)
        load_sound("goal_sound")
    def render(self, screen, text_game_image=None):
        screen.blit(cut_scene,(0,0))
        screen.blit(panel_image,panel_image.get_rect(center = (screen_width/2,screen_height/2)))
        screen.blit(text_game_image,text_game_image.get_rect(center = (screen_width/2,200)))
        text = 'Seviye Atladın!\nDevam etmek için Boşluk tuşuna basın'
        blit_text(screen,text,(377,330),self.font,color=(255,255,255))
    def update(self,screen):
        pass
    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                set_time(pygame.time.get_ticks()/1000)
                self.manager.go_to(StoreScene())

class FailureScene(object):
    def __init__(self):
        super(FailureScene, self).__init__()
        write_high_score(get_score())
        load_sound("made_goal_sound")
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Libre.ttf'), 24)
    def render(self, screen):
        screen.blit(cut_scene,(0,0))
        screen.blit(panel_image,panel_image.get_rect(center = (screen_width/2,screen_height/2)))
        screen.blit(text_game_image,text_game_image.get_rect(center = (screen_width/2,200)))
        text = 'Yeterli puana ulaşamadınız!\nYeniden başlamak için Boşluk tuşuna basın'
        blit_text(screen,text,(377,350),self.font,color=(255,255,255))
    def update(self,screen):
        pass
    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.manager.go_to(StartScene())

class WinScene(object):
    def __init__(self):
        super(WinScene, self).__init__()
        write_high_score(get_score())
        load_sound("goal_sound")
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Libre.ttf'), 24)
    def render(self, screen):
        screen.blit(cut_scene,(0,0))
        screen.blit(panel_image,panel_image.get_rect(center = (screen_width/2,screen_height/2)))
        screen.blit(text_game_image,text_game_image.get_rect(center = (screen_width/2,200)))
        text = 'Bu oyunu kazandınız!\nYeniden başlamak için Boşluk tuşuna basın'
        blit_text(screen,text,(377,300),self.font,color=(255,255,255))
    def update(self,screen):
        pass
    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.manager.go_to(StartScene())

class HighScoreScene(object):
    def __init__(self):
        super(HighScoreScene, self).__init__()
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Libre.ttf'), 24)
        self.continute = Button(1050,50,continue_img,0.5)
    def render(self, screen):
        screen.blit(cut_scene,(0,0))
        screen.blit(panel_image,panel_image.get_rect(center = (screen_width/2,screen_height/2)))
        screen.blit(text_game_image,text_game_image.get_rect(center = (screen_width/2,200)))
        screen.blit(self.font.render('YÜKSEK SKOR', True, (255, 255, 255)), (560, 300))
        self.continute.render(screen)
        text = get_high_score_as_text()
        blit_text(screen,text,(377,350),self.font,color=(255,255,255))
    def update(self,screen):
        pass
    def handle_events(self, events):
        if self.continute.is_click():
            self.manager.go_to(StartScene())

class StoreScene(object):
    def __init__(self):
        super(StoreScene, self).__init__()
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Libre.ttf'), 28)
        self.shopkeeper = Shopkeeper(900,250)
        self.continute = Button(1050,50,continue_img,0.5)

        self.rock_collectors_book = Button(87,420,rock_collectors_book,2)
        self.is_rock = random.randint(0,1)
        if self.is_rock:
            self.rock_price = random.randint(10,150)

        self.strength_drink = Button(300,400,strength_drink,2)
        self.is_strength_drink = random.randint(0,1)
        if self.is_strength_drink:
            self.strength_drink_price = random.randint(0,300)+100

        self.gem_polish = Button(500,440,gem_polish,2)
        self.is_gem_polish = random.randint(0,1)
        if self.is_gem_polish:
            self.gem_polish_price = random.randint(0,get_level()*100) +200

        self.clover = Button(650,420,clover,2)
        self.is_clover = random.randint(0,1)
        if self.is_clover:
            self.clover_price = random.randint(0,get_level()*50) + get_level()*2 + 1

        self.dynamite = Button(800,425,dynamite_shop,2)
        self.is_dynamite = random.randint(0,1)
        if self.is_dynamite:
            self.dynamite_price = random.randint(0,300) + 1 + get_level()*2

        self.text = 'Bir şey yapmak için tıklayın\nBir şey söylemek için tıklayın ve tıklayın'
        self.is_buy = False

        self.buyTNT = 0
        self.buyRock = False
        self.buyGem = False
        self.buyClover = False
        self.buyDrink = 1
    def render(self, screen):
        screen.blit(store_BG,(0,0))
        screen.blit(self.font.render("Para: "+str(get_score()), True, (0, 0, 0)), (5, 0))
        self.shopkeeper.draw(screen)
        screen.blit(table_image,table_image.get_rect(bottom = screen_height))
        screen.blit(dialog_image,(220,100))
        self.continute.render(screen)
        if self.is_rock:
            self.rock_collectors_book.render(screen)
            blit_nor_text(screen,"$"+str(self.rock_price),(140,565),self.font,color=(0,150,0))
        if self.is_strength_drink:
            self.strength_drink.render(screen)
            blit_nor_text(screen,"$"+str(self.strength_drink_price),(350,565),self.font,color=(0,150,0))
        if self.is_gem_polish:
            self.gem_polish.render(screen)
            blit_nor_text(screen,"$"+str(self.gem_polish_price),(550,565),self.font,color=(0,150,0))
        if self.is_clover:
            self.clover.render(screen)
            blit_nor_text(screen,"$"+str(self.clover_price),(690,565),self.font,color=(0,150,0))
        if self.is_dynamite:
            self.dynamite.render(screen)
            blit_nor_text(screen,"$"+str(self.dynamite_price),(820,565),self.font,color=(0,150,0))
        blit_text(screen,self.text,(250,110),self.font,color=(0,0,0))
    def update(self,screen): #handel hover
        if self.is_rock:
            if self.rock_collectors_book.is_hover():
                text = "Taş Koleksiyoncuları Kitabı. Bir sonraki seviyede taşın değeri\üç kat daha fazla olacak.\nYalnızca 1. seviye için geçerlidir."
                blit_text(screen,text,(250,620),self.font,color=(255,255,255))
        if self.is_strength_drink:
            if self.strength_drink.is_hover():
                text = "Enerji içeceği. Eşya çekme hızınız bir sonraki seviyede\nbiraz daha hızlı olacaktır.\nİçecekler yalnızca bir seviye boyunca geçerlidir.p độ."
                blit_text(screen,text,(250,620),self.font,color=(255,255,255))
        if self.is_gem_polish:
            if self.gem_polish.is_hover():
                text = "Değerli taşların parlatılması. Bir sonraki seviyede\nmücevherler ve elmaslar daha yüksek bir değere sahip olacak.\nYalnızca 1 seviye için geçerlidir."
                blit_text(screen,text,(250,620),self.font,color=(255,255,255))
        if self.is_clover:
            if self.clover.is_hover():
                text = "Şanslı yonca. Bu eşya bir sonraki seviyede çantadan\niyi bir şey alma şansını artıracaktır.\nYalnızca 1 seviye için geçerlidir."
                blit_text(screen,text,(250,620),self.font,color=(255,255,255))
        if self.is_dynamite:
            if self.dynamite.is_hover():
                text = "Değersiz bir şey çektikten sonra\nyukarı tuşuna basarak üzerine bir parça dinamit atıp onu havaya uçurun."
                blit_text(screen,text,(250,620),self.font,color=(255,255,255))
    def handle_events(self, events):
        if self.is_rock:
            if self.rock_collectors_book.is_click():
                if buy_item(1,self.rock_price):
                    self.is_buy = True
                    self.buyRock = True
                    self.is_rock = False
        if self.is_strength_drink:
            if self.strength_drink.is_click():
                if buy_item(2,self.strength_drink_price):
                    self.is_buy = True
                    self.buyDrink = 2
                    self.is_strength_drink = False
        if self.is_gem_polish:
            if self.gem_polish.is_click():
                if buy_item(3,self.gem_polish_price):
                    self.is_buy = True
                    self.buyGem = True
                    self.is_gem_polish = False
        if self.is_clover:
            if self.clover.is_click():
                if buy_item(4,self.clover_price):
                    self.is_buy = True
                    self.buyClover = True
                    self.is_clover = False
        if self.is_dynamite:
            if self.dynamite.is_click():
                if buy_item(5,self.dynamite_price):
                    self.is_buy = True
                    self.buyTNT =1
                    self.is_dynamite = False
        if self.continute.is_click():
            if not(self.is_buy):
                # self.shopkeeper.current_frame = 1
                # self.render(screen)
                # pygame.time.wait(2000)
                pass #need fix
            self.start(self.buyTNT,self.buyDrink,self.buyClover,self.buyGem,self.buyRock)
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.start(self.buyTNT,self.buyDrink,self.buyClover,self.buyGem,self.buyRock)
    def start(self,tnt=0,speed=1,clover =0,gem =0, rock =0):
            set_time(pygame.time.get_ticks()/1000)
            self.manager.go_to(GameScene(get_level(),tnt,speed,clover,gem,rock))
class GameScene(Scene):
    def __init__(self, level, tnt=0, speed=1, is_clover=False, is_gem=False, is_rock=False):
        super(GameScene, self).__init__()
        self.level = level
        self.miner = Miner(620, -7, 5)
        self.rope = Rope(643, 45, 300, hook_images, tnt, speed)
        self.bg, self.items = load_level(random_level(self.level), is_clover, is_gem, is_rock)
        # self.bg,self.items = load_level("LDEBUG")
        self.play_Explosive = False
        self.explosive = None
        self.text_font = pygame.font.Font(os.path.join("assets", "fonts", 'Libre.ttf'), 14)
        self.timer = 0
        self.pause_time = 0
        self.pause = False
        self.exit_button = Button(1050, 5, exit_image, 0.25)
        self.next_button = Button(950, 0, next_image, 0.4)

    def render(self, screen):
        dt = clock.tick(60) / 1000
        if (self.miner.state == 1):
            for item in self.items:
                if is_collision(self.rope, item):
                    self.rope.item = item
                    self.rope.item.is_move = False
                    if item.is_explosive == True:
                        # pygame.mixer.stop()
                        load_sound("explosive_sound")
                        explosive_item(item, self.items)
                    self.rope.state = 'retracting'
                    self.items.remove(item)
                    break
        if self.rope.state == 'retracting' and not (self.rope.is_use_TNT):
            self.miner.state = 2
        screen.blit(bg_top, (0, 0))
        screen.blit(self.bg, (0, 72))
        self.exit_button.render(screen)
        self.next_button.render(screen)
        # Draw item
        for item in self.items:
            item.draw(dt, screen)

        if (self.play_Explosive == True and self.explosive != None):
            # pygame.mixer.stop()
            # explosive_sound.play()
            load_sound("explosive_sound")
            self.explosive.draw(screen)
            self.explosive.update(dt)
            if (self.explosive.is_exit):
                del self.explosive
                self.play_Explosive = False
                self.miner.is_TNT = False
                self.miner.state = 0
                self.rope.is_use_TNT = False
        for i in range(self.rope.have_TNT):
            screen.blit(dynamite_image, (725 + i * 25, 10))
        # Update sprite
        self.miner.update(dt)
        self.miner.draw(screen)
        self.rope.update(self.miner, dt, screen)
        self.rope.draw(screen)
        draw_point(self.rope, dt, self.miner)

        def update(self, screen):
            self.timer = 60 - int(pygame.time.get_ticks() / 1000 - get_time())
            screen.blit(self.text_font.render("Para:", True, (0, 0, 0)), (5, 0))
            screen.blit(self.text_font.render("$" + str(get_score()), True, (0, 150, 0)), (55, 0))
            screen.blit(self.text_font.render("Hedef", True, (0, 0, 0)), (5, 25))
            screen.blit(self.text_font.render("$" + str(get_goal()), True, (255, 150, 0)), (96, 25))
            screen.blit(self.text_font.render("Geçen Süre", True, (0, 0, 0)), (1140, 0))
            screen.blit(self.text_font.render(str(self.timer), True, (255, 100, 7)), (1240, 0))
            screen.blit(self.text_font.render("Seviye", True, (0, 0, 0)), (1140, 25))
            screen.blit(self.text_font.render(str(self.level), True, (255, 100, 7)), (1190, 25))
        def next_level(self):
            if get_score() > get_goal():
                set_level(get_level() + 1)
                if get_level() > 10:
                    self.manager.go_to(WinScene())
                    return
                set_goal(get_goal() + get_level() * goalAddOn)
                self.manager.go_to(FinishScene())
            else:
                set_level(1)
                set_goal(650)
                self.manager.go_to(FailureScene())

        def handle_events(self, events):
            if (self.timer < 0):
                self.next_level()
            for e in events:
                if self.exit_button.is_click():
                    self.manager.go_to(StartScene())
                if self.next_button.is_click():
                    self.next_level()
                if e.type == pygame.QUIT:
                    write_high_score(get_score())
                    pygame.quit()
                    sys.exit(0)
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:  # PAUSE and UNPAUSE
                        self.pause = not (self.pause)
                        if self.pause:  # PAUSE
                            self.pause_time = pygame.time.get_ticks() / 1000
                            set_pause(True)
                        else:  # UNPAUSE
                            set_pause(False)
                            set_time(get_time() + pygame.time.get_ticks() / 1000 - self.pause_time)
                    if e.key == pygame.K_ESCAPE:
                        self.next_level()
                    if (e.key == pygame.K_DOWN and self.rope.timer <= 0):  # expanding
                        self.miner.state = 1
                    if e.key == pygame.K_UP:  # retracting
                        if (self.rope.have_TNT > 0 and self.rope.item != None):
                            self.rope.is_use_TNT = True
                            self.miner.state = 4
                            self.explosive = Explosive(self.rope.x2 - 128, self.rope.y2 - 128, 12)
                            self.play_Explosive = True
                            self.rope.have_TNT -= 1
                            self.rope.length = 50
                            self.miner.is_TNT = True

