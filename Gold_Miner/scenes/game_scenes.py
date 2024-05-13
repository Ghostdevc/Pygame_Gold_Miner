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
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Fernando.ttf'), 28)
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
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Fernando.ttf'), 24)
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
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Fernando.ttf'), 24)
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
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Fernando.ttf'), 24)
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

