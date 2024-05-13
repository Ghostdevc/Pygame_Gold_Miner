import os

import pygame
from definitions import *
from entities.gold import Gold
from entities.tnt import TNT
from entities.others import Other
from entities.rock import Rock
from entities.mole import Mole
from entities.question import QuestionBag
import datetime


# Döngü ve nesne arasındaki çarpışmayı kontrol et
def is_collision(rope, item):
    if rope.hook.rect.colliderect(item.rect) and rope.state == 'expanding':
        return True
    return False


# Patlayıcı nesne işlemini gerçekleştir
def explosive_item(tnt, items):
    items_to_remove = []
    for item in items:
        if item == tnt:
            continue
        if math.sqrt(pow(abs(item.x - tnt.x), 2) + pow(abs(item.y - tnt.y), 2)) < 200:
            items_to_remove.append(item)
    for item in items_to_remove:
        items.remove(item)


# Nesne yükleme işlemi
def load_item(item_data, is_clover=False, is_gem=False, is_rock=False):
    item_name = item_data["type"]
    x = item_data["pos"]["x"]
    y = item_data["pos"]["y"]
    item = None
    match item_name:
        case "MiniGold":
            item = Gold(x, y, 30, MiniGold_point)
        case "NormalGold":
            item = Gold(x, y, 70, NormalGold_point)
        case "NormalGoldPlus":
            item = Gold(x, y, 90, NormalGoldPlus_point)
        case "BigGold":
            item = Gold(x, y, 150, BigGold_point)
        case "MiniRock":
            if is_rock:
                item = Rock(x, y, 30, MiniRock_point * 3)
            else:
                item = Rock(x, y, 30, MiniRock_point)
        case "NormalRock":
            if is_rock:
                item = Rock(x, y, 60, NormalRock_point * 3)
            else:
                item = Rock(x, y, 60, NormalRock_point)
        case "QuestionBag":
            if is_clover:
                item = QuestionBag(x, y, lucky=2)
            else:
                item = QuestionBag(x, y, lucky=1)
        case "Diamond":
            if is_gem:
                item = Other(x, y, diamond_image, int(Diamond_point * 1.5))
            else:
                item = Other(x, y, diamond_image, Diamond_point)
        case "Mole":
            item = Mole(x, y, mole_image, Mole_point, direction=item_data["dir"])
        case "MoleWithDiamond":
            if is_gem:
                item = Mole(x, y, mole2_image, int(Diamond_point * 1.5) + 2, direction=item_data["dir"])
            else:
                item = Mole(x, y, mole2_image, MoleWithDiamond_point, direction=item_data["dir"])
        case "Skull":
            item = Other(x, y, skull_image, Skull_point)
        case "Bone":
            item = Other(x, y, bone_image, Bone_point)
        case "TNT":
            item = TNT(x, y)
        case _:
            print("None")
            item = None
    return item


# Nesneleri yükle
def load_items(items_data, is_clover=False, is_gem=False, is_rock=False):
    items = []
    for item in items_data:
        items.append(load_item(item, is_clover, is_gem, is_rock))
    return items

def load_sound(sound_name):
    sound_path = os.path.join("assets", "sounds", f"{sound_name}.wav")
    return pygame.mixer.Sound(sound_path)

# Seviye yükleme işlemi
def load_level(level, is_clover, is_gem, is_rock):
    bg_name = None
    bg = None
    file_path = "levels.json"
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        bg_name = data[level]['type']
        match bg_name:
            case "LevelA":
                bg = bgA
            case "LevelB":
                bg = bgB
            case "LevelC":
                bg = bgC
            case "LevelD":
                bg = bgD
            case "LevelE":
                bg = bgA
            case _:
                bg = bgA
    except:
        print("No file levels.json!")
        sys.exit(0)
    return bg, load_items(data[level]['entities'], is_clover, is_gem, is_rock)


# Rastgele seviye oluştur
def random_level(level_number):
    ran_level = random.randint(1, 3)
    level_text = "L" + str(level_number) + "_" + str(ran_level)
    return level_text


# Puanı ekrana çiz
def draw_point(rope, dt, miner):
    if rope.text == "dynamite" and rope.text_direction != "None":
        rope.time_text -= dt
        if rope.x_text > 500:
            rope.text_size += dt * rope.speed / 5

pygame.mixer.set_num_channels(8)
voice1 = pygame.mixer.Channel(1)
voice2 = pygame.mixer.Channel(2)
voice3 = pygame.mixer.Channel(3)
voice4 = pygame.mixer.Channel(4)
voice5 = pygame.mixer.Channel(5)
voice6 = pygame.mixer.Channel(6)
def load_sound(sound_name):
    match sound_name:
        case "explosive_sound":
            pygame.mixer.stop()
            voice1.play(explosive_sound)
        case "goal_sound":
            pygame.mixer.stop()
            voice2.play(goal_sound)
        case "grab_back_sound":
            voice4.stop()
            if not voice3.get_busy():
                voice3.play(grab_back_sound)
        case "grab_start_sound":
            if not voice4.get_busy():
                voice4.play(grab_start_sound)
        case "hook_reset_sound":
            voice3.stop()
            if not voice5.get_busy() or not voice1.get_busy():
                voice5.play(hook_reset_sound)
        case "high_value_sound":
            high_value_sound.play()
        case "normal_value_sound":
            normal_value_sound.play()
        case "money_sound":
            money_sound.play()
        case "made_goal_sound":
            pygame.mixer.stop()
            made_goal_sound.play()

