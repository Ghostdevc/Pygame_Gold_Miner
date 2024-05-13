import pygame
def load_images(filepaths, is2x = False):
    images = []
    for filepath in filepaths:
        image = pygame.image.load(filepath)
        if is2x:
            image = pygame.transform.scale2x(image)
        images.append(image)
    return images

#Game Setting


screen_width = 1280
screen_height = 820
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")

#Entities

gold_image = pygame.image.load("./assets/images/gold.png")
rock_image = pygame.image.load("./assets/images/rock.png")
mole_image = pygame.image.load("./assets/images/mole.png")
mole2_image = pygame.image.load("./assets/images/moleDiamond.png")
skull_image = pygame.image.load("./assets/images/skull.png")
bone_image = pygame.image.load("./assets/images/bone.png")
diamond_image = pygame.image.load("./assets/images/diamond.png")
tnt_image = pygame.image.load("./assets/images/tnt.png")
empty = pygame.image.load('./assets/images/empty.png')
questionBag = pygame.image.load('./assets/images/question_bag.png')
dynamite_image = pygame.image.load('./assets/images/dynamite.png')

#Miner man
miner_files = [
    "./assets/images/miner_01.png",
    "./assets/images/miner_02.png",
    "./assets/images/miner_03.png",
    "./assets/images/miner_04.png",
    "./assets/images/miner_05.png",
    "./assets/images/miner_06.png",
    "./assets/images/miner_07.png",
    "./assets/images/miner_08.png"
]
miner_images = load_images(miner_files)

# Angry man

shopkeeper_files = [
    "./assets/images/shopkeeper_01.png",
    "./assets/images/shopkeeper_02.png"
]

shopkeeper_images = load_images(shopkeeper_files)

#Patlama
explosive_files = [
    "./assets/images/ex1.png",
    "./assets/images/ex2.png",
    "./assets/images/ex3.png",
    "./assets/images/ex4.png",
    "./assets/images/ex5.png",
    "./assets/images/ex6.png",
    "./assets/images/ex7.png",
    "./assets/images/ex8.png",
    "./assets/images/ex9.png"
]
explosive_images = load_images(explosive_files,True)

#kanca
hook_files = [
    "./assets/images/kanca_01.png",
    "./assets/images/kanca_02.png",
    "./assets/images/kanca_03.png"
]
hook_images = load_images(hook_files)
hight_score = pygame.image.load('./assets/images/hight_score.png')
panel_image = pygame.image.load('./assets/images/panel.png')
table_image = pygame.image.load('./assets/images/shop_table.png')
dialog_image = pygame.image.load('./assets/images/ui_dialog.png')
continue_img = pygame.image.load('./assets/images/continue.png')



#Shop item

rock_collectors_book = pygame.image.load('./assets/images/rock_collectors_book.png')
strength_drink = pygame.image.load('./assets/images/strength_drink.png')
gem_polish = pygame.image.load('./assets/images/gem_polish.png')
clover = pygame.image.load('./assets/images/clover.png')
dynamite_shop = pygame.image.load('./assets/images/dynamite_shop.png')
exit_image = pygame.image.load('./assets/images/exit.png')
next_image = pygame.image.load('./assets/images/next.png')

#Background
bgA = pygame.image.load('./assets/images/bg_level_A.jpg').convert()
bgA = pygame.transform.scale2x(bgA)
bgB = pygame.image.load('./assets/images/bg_level_B.jpg').convert()
bgB = pygame.transform.scale2x(bgB)
bgC = pygame.image.load('./assets/images/bg_level_C.jpg').convert()
bgC = pygame.transform.scale2x(bgC)
bgD = pygame.image.load('./assets/images/bg_level_D.jpg').convert()
bgD = pygame.transform.scale2x(bgD)
bg_top = pygame.image.load('./assets/images/bg_top.png').convert()
cut_scene = pygame.image.load('./assets/images/cut_scene.jpg').convert()
miner_menu = pygame.image.load('./assets/images/miner_menu.png')
miner_menu_rect  = miner_menu.get_rect(bottomright=(screen_width,screen_height))
start_BG = pygame.image.load('./assets/images/start_BG.jpg')
store_BG = pygame.image.load('./assets/images/bg_shop.png')

#Sounds
pygame.mixer.pre_init(frequency=11025, size=-16, channels=8, buffer=2048)
pygame.init()
explosive_sound = pygame.mixer.Sound('./assets/audios/explosive.wav')
goal_sound = pygame.mixer.Sound('./assets/audios/goal.wav')
grab_back_sound = pygame.mixer.Sound('./assets/audios/grab_back.wav')
grab_start_sound = pygame.mixer.Sound('./assets/audios/grab_start.wav')
hook_reset_sound = pygame.mixer.Sound('./assets/audios/hook_reset.wav')
high_value_sound = pygame.mixer.Sound('./assets/audios/high_value.wav')
normal_value_sound = pygame.mixer.Sound('./assets/audios/normal_value.wav')
money_sound = pygame.mixer.Sound('./assets/audios/money.wav')
made_goal_sound = pygame.mixer.Sound('./assets/audios/made_goal.wav')

#Puanlamalar
MiniGold_point = 50
NormalGold_point  = 100
NormalGoldPlus_point = 250
BigGold_point = 500
MiniRock_point = 10
NormalRock_point = 20
BigRock_point = 100
Diamond_point = 600
Mole_point = 5
MoleWithDiamond_point = 605
Skull_point = 20
Bone_point = 5

