import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

text_font = pygame.font.SysFont("Arial", 30)

class Dice(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))

dice_images = [pygame.image.load(f'Graphics/Dice/d{i}.png').convert_alpha() for i in range(1, 7)]
dice_images = [pygame.transform.scale(image, (100, 100)) for image in dice_images]

dice_sprites = pygame.sprite.Group()

def type_text(text, font, text_col, x, y):
    img = font.render(str(text), True, text_col)
    screen.blit(img, (x, y))

def dice_roll():
    global dice_value, dice1
    dice1 = random.randint(1, 6)
    dice_value = int(dice1)
    return dice_value, dice1

def display_dice(center_x, center_y):
    dice_sprites.empty()
    dice1_sprite = Dice(dice_images[dice1 - 1], center_x, center_y)
    dice_sprites.add(dice1_sprite)
    dice_sprites.draw(screen)
    pygame.display.update()
    type_text(f"Press R to roll dice", text_font, (0, 0, 0), center_x - 95, center_y - 110)
    type_text(f"Dice Value: {dice_value}", text_font, (0, 0, 0), center_x - 65, center_y + 110)
    pygame.display.update()

dice_value = 0
dice1 = 0

def main():
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    dice_roll()
                    display_dice(center_x, center_y)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
