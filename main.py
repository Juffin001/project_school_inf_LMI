import pygame
import time
from Buttons import *
from back import *

pygame.init()
FPS = 60
screen_sizes = [[500, 500], [1920, 1080], [2560, 1440], [3440, 1440], [2160, 1620]]
screen_size_choose = 0
screen_size = screen_sizes[screen_size_choose]
dis = pygame.display.set_mode((screen_size[0], screen_size[1]), pygame.RESIZABLE)
pygame.display.set_caption('ProjectMagdeev')
clock = pygame.time.Clock()

icon = pygame.image.load('images/awesome_icon.bmp')

sizes_dict = dict()
sizes_dict = {
    '0_main': [250, 250],
    '0_settings': [250, 350],
    '0_back': [30, 470],
    '1_main': [500, 500],
    '1_settings': [700, 700],
    '1_back': [700, 700],
    '2_main': '',
    '2_settings': '',
    '2_back': '',
    '3_main': '',
    '3_settings': '',
    '3_back': '',
    '4_main': '',
    '4_settings': '',
    '4_back': '',
}
if screen_size_choose == 0:
    settings_button = Button((sizes_dict.get('0_settings'))[0], (sizes_dict.get('0_settings'))[1], 'images/ultimate_settings_button.png')
    main_button = Button((sizes_dict.get('0_main'))[0], (sizes_dict.get('0_main'))[1], 'images/unique_main_button.png')
    back_button = Button((sizes_dict.get('0_back'))[0], (sizes_dict.get('0_back'))[1], 'images/back_button.png')
    screen_size_change_button = Button((sizes_dict.get('0_main'))[0], (sizes_dict.get('0_main'))[1], 'images/screen_size_change_button_0.png')
elif screen_size_choose == 1:
    settings_button = Button((sizes_dict.get('1_settings'))[0], (sizes_dict.get('1_settings'))[1], 'images/ultimate_settings_button.png')
    main_button = Button((sizes_dict.get('1_main'))[0], (sizes_dict.get('1_main'))[1], 'images/unique_main_button.png')
    back_button = Button((sizes_dict.get('1_back'))[0], (sizes_dict.get('1_back'))[1], 'images/back_button.png')
    screen_size_change_button = Button((sizes_dict.get('1_main'))[0], (sizes_dict.get('1_main'))[1], 'images/screen_size_change_button_0.png')
elif screen_size_choose == 2:
    settings_button = Button((sizes_dict.get('2_settings'))[0], (sizes_dict.get('2_settings'))[1], 'images/ultimate_settings_button.png')
    main_button = Button((sizes_dict.get('2_main'))[0], (sizes_dict.get('2_main'))[1], 'images/unique_main_button.png')
    back_button = Button((sizes_dict.get('2_back'))[0], (sizes_dict.get('2_back'))[1], 'images/back_button.png')
    screen_size_change_button = Button((sizes_dict.get('2_main'))[0], (sizes_dict.get('2_main'))[1], 'images/screen_size_change_button_0.png')
elif screen_size_choose == 3:
    settings_button = Button((sizes_dict.get('3_settings'))[0], (sizes_dict.get('3_settings'))[1], 'images/ultimate_settings_button.png')
    main_button = Button((sizes_dict.get('3_main'))[0], (sizes_dict.get('3_main'))[1], 'images/unique_main_button.png')
    back_button = Button((sizes_dict.get('3_back'))[0], (sizes_dict.get('3_back'))[1], 'images/back_button.png')
    screen_size_change_button = Button((sizes_dict.get('0_main'))[0], (sizes_dict.get('0_main'))[1], 'images/screen_size_change_button_0.png')
elif screen_size_choose == 4:
    settings_button = Button((sizes_dict.get('4_settings'))[0], (sizes_dict.get('4_settings'))[1], 'images/ultimate_settings_button.png')
    main_button = Button((sizes_dict.get('4_main'))[0], (sizes_dict.get('4_main'))[1], 'images/unique_main_button.png')
    back_button = Button((sizes_dict.get('4_back'))[0], (sizes_dict.get('4_back'))[1], 'images/back_button.png')
    screen_size_change_button = Button((sizes_dict.get('0_main'))[0], (sizes_dict.get('0_main'))[1], 'images/screen_size_change_button_0.png')

menu_bg = Background('images/beatiful_minimalistck_background.png', [0,0])
main_bg = Background('images/important_programm.png', [0,0])
settings_bg = Background('images/settings_bg.png', [0,0])

pygame.display.set_icon(icon)

is_settings = False
is_main_programm = False
is_menu = True
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and is_menu:
            x, y = event.pos
            if settings_button.collide_point(x, y):
                is_settings = True
                is_menu = False
            elif main_button.collide_point(x, y):
                is_main_programm = True
                is_menu = False
        if event.type == pygame.MOUSEBUTTONDOWN and (is_settings or is_main_programm):
            x, y = event.pos
            if back_button.collide_point(x, y):
                is_menu = True
                is_settings = False
                is_main_programm = False
        if event.type == pygame.MOUSEBUTTONDOWN and is_settings:
            x, y = event.pos
            if screen_size_change_button.collide_point(x, y):
                if screen_size != 4:
                    screen_size_choose += 1
                else:
                    screen_size = 0




    if is_menu:
        dis.blit(menu_bg.image, menu_bg.rect)
        dis.blit(settings_button.image, settings_button.rect)
        dis.blit(main_button.image, main_button.rect)
    if is_settings:
        dis.blit(settings_bg.image, settings_bg.rect)
        dis.blit(back_button.image, back_button.rect)
        dis.blit(screen_size_change_button.image, screen_size_change_button.rect)
    if is_main_programm:
        dis.blit(main_bg.image, main_bg.rect)
        dis.blit(back_button.image, back_button.rect)
    pygame.display.update()
    clock.tick(FPS)
exit()
