import pygame
from sys import exit
import random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Dice Roll Stimulator")

background_image = pygame.image.load('graphics/background2.png')
font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
roll_message = font.render("press SPACEBAR to start rolling", True, (255, 235, 193))

dice_images = []
dice_rolling_images = []

# since there are 6 dice images
for num in range(1, 7):
    dice_image = pygame.image.load('graphics/dice/' + str(num) + '.png')
    dice_images.append(dice_image)

# since there are 8 rolling dice images
for num in range(1, 9):
    dice_rolling_image = pygame.image.load('graphics/animation/roll' + str(num) + '.png')
    dice_rolling_images.append(dice_rolling_image)

rolling_aud = pygame.mixer.Sound('audio/roll_aud.mp3')
rolling_stop_aud = pygame.mixer.Sound('audio/roll_stop_aud.mp3')

is_rolling = False
rolling_images_counter = 0
dice_num_image = dice_images[0]
first = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background_image, (0, 0))
    screen.blit(roll_message, (50, 300))

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and is_rolling is False:
        is_rolling = True
        rolling_aud.play()
        rand_num = random.randint(0, 5)
        dice_num_image = dice_images[rand_num]
        screen.blit(dice_rolling_images[rolling_images_counter], (250, 150))
        rolling_images_counter += 1
        first = True

        # start rolling and calculate dice num
    else:
        if is_rolling:
            # showing rolling animation images
            screen.blit(dice_rolling_images[rolling_images_counter], (250, 150))
            rolling_images_counter += 1
            if rolling_images_counter >= 8:
                is_rolling = False
                rolling_images_counter = 0

        else:
            screen.blit(dice_num_image, (250, 150))
            if first:
                rolling_stop_aud.play()
                first = False
            # show the dice which contains a number

    pygame.display.update()
    clock.tick(13)
