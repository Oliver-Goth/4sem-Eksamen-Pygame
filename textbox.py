import pygame
from sys import exit
import random

class DiceRollSimulator:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Dice Roll Simulator")

        self.dice_images = []
        self.dice_rolling_images = []

        for num in range(1, 7):
            dice_image = pygame.image.load('Graphics/Animation/Dice/d' + str(num) + '.png')
            self.dice_images.append(dice_image)

        for num in range(1, 9):
            dice_rolling_image = pygame.image.load('Graphics/Animation/Dice/roll' + str(num) + '.png')
            self.dice_rolling_images.append(dice_rolling_image)

        self.rolling_aud = pygame.mixer.Sound('audio/roll_aud.mp3')
        self.rolling_stop_aud = pygame.mixer.Sound('audio/roll_stop_aud.mp3')

        self.is_rolling = False
        self.rolling_images_counter = 0
        self.dice_num_image = self.dice_images[0]
        self.first = True

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and not self.is_rolling:
                self.is_rolling = True
                self.rolling_aud.play()
                rand_num = random.randint(0, 5)
                self.dice_num_image = self.dice_images[rand_num]
                self.screen.blit(self.dice_rolling_images[self.rolling_images_counter], (250, 150))
                self.rolling_images_counter += 1
                self.first = True
            else:
                if self.is_rolling:
                    self.screen.blit(self.dice_rolling_images[self.rolling_images_counter], (250, 150))
                    self.rolling_images_counter += 1
                    if self.rolling_images_counter >= 8:
                        self.is_rolling = False
                        self.rolling_images_counter = 0
                else:
                    self.screen.blit(self.dice_num_image, (250, 150))
                    if self.first:
                        self.rolling_stop_aud.play()
                        self.first = False

            pygame.display.update()
            self.clock.tick(13)

# To run the simulator, you can use the following code:
if __name__ == "__main__":
    simulator = DiceRollSimulator()
    simulator.run()
