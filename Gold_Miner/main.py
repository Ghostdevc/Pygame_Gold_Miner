from definitions import *
from utility import *

pygame.init()

#GAME LOOP
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    draw_background(bgA, bg_top, screen)

    pygame.display.update()

    clock.tick(FPS)


pygame.quit()