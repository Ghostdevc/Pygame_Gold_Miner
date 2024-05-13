import os

from scenes.game_scenes import *
import pygame


def main():
    pygame.init()
    running = True
    manager = SceneMananger()
    font = pygame.font.Font(os.path.join("assets", "fonts", 'Libre.ttf'), 28)
    while running:
        if pygame.event.get(pygame.QUIT):
            write_high_score(get_score())
            running = False
            return
        manager.scene.handle_events(pygame.event.get())

        if get_pause() == False:
            manager.scene.render(screen)
            manager.scene.update(screen)
        else:
            screen.blit(panel_image,panel_image.get_rect(center = (screen_width/2,screen_height/2)))
            text = font.render('Devam etmek için Boşluk tuşuna basın', True, (255, 255, 255))
            screen.blit(text,text.get_rect(center = (screen_width/2,screen_height/2)))

        pygame.display.flip()

if __name__ == "__main__":
    main()