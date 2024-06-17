import pygame
import Cashcow_Board
from Cashcow_Dice import dice_roll, display_dice

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1500, 1000
CELL_WIDTH, CELL_HEIGHT = 100, 100
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 50
BOARD_COLOR = (232, 228, 214)
LINE_COLOR = (0, 0, 0)
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (220, 220, 220)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 215, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

font = pygame.font.SysFont(None, 40)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Cashcow Game")

def draw_button():
    pygame.draw.rect(screen, GRAY, (0, 0, BUTTON_WIDTH, BUTTON_HEIGHT))
    text = font.render("Menu", True, BLACK)
    text_rect = text.get_rect(center=(BUTTON_WIDTH // 2, BUTTON_HEIGHT // 2))
    screen.blit(text, text_rect)

def main():
    global player_track
    
    clock = pygame.time.Clock()

    dice_value, dice1 = dice_roll()

if __name__ == "__main__":
    Cashcow_Board.main()