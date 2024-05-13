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
def draw_point(rope,dt,miner):
    if rope.text == "dynamite" and rope.text_direction !="None":
        rope.time_text -= dt
        if rope.x_text > 500:
            rope.text_size += dt*rope.speed /(5)
        elif rope.text_size > 30 and rope.text_size < 46:
            rope.time_text = 0.4
            rope.text_size -= dt*rope.speed /(5)
        elif rope.text_size > 16 and rope.time_text < 0:
            rope.text_size -= dt*rope.speed /(25)
        if rope.time_text < 0:
            if rope.text_direction == "left":
                rope.x_text -= dt * rope.speed
                if rope.x_text <= 500:  # Reached left boundary, change direction
                    rope.text_direction = "right"
            elif rope.text_direction == "right":
                rope.x_text += dt * rope.speed
                if rope.x_text >= 700:  # Reached right boundary, change direction
                    rope.text_direction = "None"
        screen.blit(dynamite_image,(rope.x_text,10))
    elif rope.text == "strength" and rope.text_direction !="None":
        rope.time_text -= dt
        miner.state = 3
        if rope.x_text > 400:
            rope.text_size += dt*rope.speed /(8)
        elif rope.text_size > 30 and rope.text_size < 46:
            rope.time_text = 0.4
            rope.text_size -= dt*rope.speed /(5)
        elif rope.text_size > 16 and rope.time_text < 0:
            rope.text_size -= dt*rope.speed
        if rope.time_text < 0:
            if rope.text_direction == "left":
                rope.x_text -= dt * rope.speed
                if rope.x_text <= 400:  # Reached left boundary, change direction
                    rope.text_direction = "right"
            elif rope.text_direction == "right":
                rope.text_size -= dt*rope.speed /(5)
                if rope.text_size <= 0:  # Reached right boundary, change direction
                    miner.state = 3
                    rope.text_direction = "None"
        text_font = pygame.font.Font(os.path.join("assets", "fonts", 'Libre.ttf'), int(rope.text_size))
        screen.blit(text_font.render("Sức mạnh", True, (0, 15, 0)), (rope.x_text, rope.y_text))
    elif rope.text != "" and rope.x_text > 120 and rope.text_direction !="None": # show tiền
        rope.time_text -= dt
        if rope.x_text > 500:
            rope.text_size += dt*rope.speed /(5)
        elif rope.text_size > 30 and rope.text_size < 46:
            rope.time_text = 0.2
            rope.text_size -= dt*rope.speed /(5)
        elif rope.text_size > 16 and rope.time_text < 0:
            rope.text_size -= dt*rope.speed /(25)
        if rope.time_text < 0:
            rope.x_text -= dt*rope.speed
        text_font = pygame.font.Font(os.path.join("assets", "fonts", 'Libre.ttf'), int(rope.text_size))
        screen.blit(text_font.render("+$"+rope.text, True, (0, 15, 0)), (rope.x_text, rope.y_text))

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
def blit_nor_text(surface, text_in, pos, font, color=pygame.Color('black')):
    text = font.render(text_in, True, color)
    surface.blit(text,text.get_rect(center = pos))
def is_enough_money(item_price):
    if item_price > get_score():
        return False
    return True
def buy_item(item_id,price):
    match item_id:
        case 1: #rock_collectors_book
            if is_enough_money(price):
                set_score(get_score()-price)
                return True
            else: return False
        case 2: #strength_drink
            if is_enough_money(price):
                set_score(get_score()-price)
                return True
            else: return False
        case 3: #gem_polish
            if is_enough_money(price):
                set_score(get_score()-price)
                return True
            else: return False
        case 4: #clover
            if is_enough_money(price):
                set_score(get_score()-price)
                return True
            else: return False
        case 5: #dynamite
            if is_enough_money(price):
                set_score(get_score()-price)
                return True
            else: return False

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

def get_high_score_from_file():
    high_scores = []
    with open(high_score_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            time_score = line.strip().split(": ")
            time = time_score[0]
            score = int(time_score[1])
            high_scores.append({"zaman": time, "puan": score})
    return high_scores
def get_high_score_as_text():
    high_scores = get_high_score_from_file()
    text = ""
    for score in high_scores:
        text += str(score["zaman"]) + "          " + str(score["puan"]) + "\n"
    if text == "":
        text = "Yüksek puan listesi bulunmamaktadır."
    return text

def write_high_score(score):
    # Dosyadan yüksek puan listesini al
    high_scores = get_high_score_from_file()
    # Şu anki zamanı al
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Yeni yüksek puanı listeye ekle
    high_scores.append({"zaman": current_time, "puan": score})

    # Puanlara göre azalan şekilde sırala
    high_scores = sorted(high_scores, key=lambda x: x["puan"], reverse=True)

    # Sadece en yüksek 3 puanı al
    high_scores = high_scores[:3]

    # Yüksek puan listesini dosyaya yaz
    with open(high_score_file, "w") as file:
        for score in high_scores:
            file.write(f"{score['zaman']}: {score['puan']}\n")
