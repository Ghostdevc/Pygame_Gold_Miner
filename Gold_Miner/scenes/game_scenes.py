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
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Teachers Students.otf'), 48)
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
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Teacher Students.otf'), 28)
        load_sound("goal_sound")
    def render(self, screen):
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
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Teacher Students.otf'), 24)
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
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Teacher Students.otf'), 24)
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
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Teacher Students.otf'), 24)
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


class GameScene(Scene):
    def __init__(self, level, tnt=0, speed=1, is_clover=False, is_gem=False, is_rock=False):
        super(GameScene, self).__init__()
        self.level = level
        self.miner = Miner(620, -7, 5)
        self.rope = Rope(643, 45, 300, hoo_images, tnt, speed)
        self.bg, self.items = load_level(random_level(self.level), is_clover, is_gem, is_rock)
        # self.bg,self.items = load_level("LDEBUG")
        self.play_Explosive = False
        self.explosive = None
        self.text_font = pygame.font.Font(os.path.join("assets", "fonts", 'Teacher Students.otf'), 14)
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

