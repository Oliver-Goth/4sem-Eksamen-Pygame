import pygame
from sys import exit
pygame.init()

#Setting the screen size
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

#Creating a screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cashcow")

#Creating the player
player = pygame.Rect((300, 250, 50, 50))

run = True
while run:

    #Setting background
    screen.fill((0,0,0))

    #Initializing Player
    pygame.draw.rect(screen, (255, 0, 0), player)

    #Movement of player
    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)

    #Event handeler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Updating the display
    pygame.display.update()

pygame.quit()