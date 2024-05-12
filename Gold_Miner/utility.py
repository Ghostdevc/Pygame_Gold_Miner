import pygame

def draw_background(background, background_top, screen):

    bg_top_height = background_top.get_height()

    screen.blit(background_top, (0, 0))
    screen.blit(background, (0, bg_top_height))
