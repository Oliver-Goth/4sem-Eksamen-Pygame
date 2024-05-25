import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

text_font = pygame.font.SysFont("Arial", 30)

dice_size = (100, 100)
dice_img1 = pygame.image.load('Graphics/Animation/Dice/d1.png').convert_alpha()
dice_img1 = pygame.transform.scale(dice_img1, dice_size)
dice_img2 = pygame.image.load('Graphics/Animation/Dice/d2.png').convert_alpha()
dice_img2 = pygame.transform.scale(dice_img2, dice_size)
dice_img3 = pygame.image.load('Graphics/Animation/Dice/d3.png').convert_alpha()
dice_img3 = pygame.transform.scale(dice_img3, dice_size)
dice_img4 = pygame.image.load('Graphics/Animation/Dice/d4.png').convert_alpha()
dice_img4 = pygame.transform.scale(dice_img4, dice_size)
dice_img5 = pygame.image.load('Graphics/Animation/Dice/d5.png').convert_alpha()
dice_img5 = pygame.transform.scale(dice_img5, dice_size)
dice_img6 = pygame.image.load('Graphics/Animation/Dice/d6.png').convert_alpha()
dice_img6 = pygame.transform.scale(dice_img6, dice_size)

def type_text(text, font, text_col, x, y):
    img = font.render(str(text), True, text_col)
    screen.blit(img, (x, y))

def dice_roll():
    global dice1, dice2, dice_value
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_value = int(dice1 + dice2)
    print(dice1, dice2, dice_value)
    return dice_value, dice1, dice2

def display_dice(center_x, center_y):
    dice1_pos = (center_x - 150, center_y)
    dice2_pos = (center_x + 50, center_y)
    
    if dice1 == 1:
        screen.blit(dice_img1, dice1_pos)
    elif dice1 == 2:
        screen.blit(dice_img2, dice1_pos)
    elif dice1 == 3:
        screen.blit(dice_img3, dice1_pos)
    elif dice1 == 4:
        screen.blit(dice_img4, dice1_pos)
    elif dice1 == 5:
        screen.blit(dice_img5, dice1_pos)
    else:
        screen.blit(dice_img6, dice1_pos)

    if dice2 == 1:
        screen.blit(dice_img1, dice2_pos)
    elif dice2 == 2:
        screen.blit(dice_img2, dice2_pos)
    elif dice2 == 3:
        screen.blit(dice_img3, dice2_pos)
    elif dice2 == 4:
        screen.blit(dice_img4, dice2_pos)
    elif dice2 == 5:
        screen.blit(dice_img5, dice2_pos)
    else:
        screen.blit(dice_img6, dice2_pos)

    type_text(f"Dice Value: {dice_value}", text_font, (0, 0, 0), center_x - 60, center_y + 110)
    pygame.display.update()