import pygame
import sys
import time
from Cashcow_Dice import dice_roll, display_dice

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1500, 1000
CELL_WIDTH, CELL_HEIGHT = 100, 100
BOARD_COLOR = (232, 228, 214)
LINE_COLOR = (0, 0, 0)
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 215, 0)
PURPLE = (128, 0, 128)

# Cell names and colors (mock names for illustration)
cell_data = [
    ("Cashflow Day", YELLOW),
    # Top Beginning
    ("Movie Theater", GREEN),
    ("Researc Center for Diseases", GREEN),
    ("Bad Partner", RED),
    ("App Development Company", GREEN),
    ("Software Co. IPO", GREEN),
    ("Coffee Shop", GREEN),
    ("400-Unit Apartment Building", GREEN),
    ("Island Vacation Rentals", GREEN),
    ("Divorce!", RED),
    ("Build Pro Golf Course", GREEN),
    ("Pizza Shop", GREEN),
    # Top END
    ("Cashflow Day", YELLOW),
    # Right Beginning
    ("Collectibles Store", GREEN),
    ("Frozen Yogurt Shop", GREEN),
    ("Bio-Tech Co. IPO", GREEN),
    ("Unforseen Repairs", RED),
    ("200-Unit Mini Storage", GREEN),
    ("Dry Cleaning Business", GREEN),
    ("Mobile Home Park", GREEN),
    # Right End
    ("Cashflow Day", YELLOW),
    # Bottom Beginning
    ("Family Resturant", GREEN),
    ("Private Wildlife Preserve", GREEN),
    ("Healthcare!", RED),
    ("Charity", PURPLE),
    ("Burger Shop", GREEN),
    ("Heat and A/C Service", GREEN),
    ("Quick Food Market", GREEN),
    ("Assisted Living Center", GREEN),
    ("Lawsuit", RED),
    ("Ticket Sales Company", GREEN),
    ("Hobby Supply Store", GREEN),
    # Bottom End
    ("Cashflow Day", YELLOW),
    # Left Beginning
    ("Fried Chicken Resturant", GREEN),
    ("Dry Dock Storage", GREEN),
    ("Beauty Salon", GREEN),
    ("Tax Audit!", RED),
    ("Auto Repair Shop", GREEN),
    ("Extreme Sports Equipment Rental", GREEN),
    ("Foreign Oil Deal", GREEN)
    # Left End
]

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Board game")

# Define the positions of each cell on the Monopoly board
cell_positions = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0),
    (12, 1),
    (12, 2),
    (12, 3),
    (12, 4),
    (12, 5),
    (12, 6),
    (12, 7),
    (12, 8), (11, 8), (10, 8), (9, 8), (8, 8), (7, 8), (6, 8), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8),
    (0, 7),
    (0, 6),
    (0, 5),
    (0, 4),
    (0, 3),
    (0, 2),
    (0, 1)
]

# Calculate the starting position to center the board
board_width = 13 * CELL_WIDTH
board_height = 9 * CELL_HEIGHT
start_x = (SCREEN_WIDTH - board_width) // 2
start_y = (SCREEN_HEIGHT - board_height) // 2

# Calculate the actual pixel positions
pixel_positions = [(start_x + x * CELL_WIDTH, start_y + y * CELL_HEIGHT) for x, y in cell_positions]

def draw_board():
    screen.fill(BOARD_COLOR)
    font = pygame.font.SysFont(None, 24)
    
    for idx, pos in enumerate(pixel_positions):
        name, color = cell_data[idx]
        pygame.draw.rect(screen, color, (*pos, CELL_WIDTH, CELL_HEIGHT))
        pygame.draw.rect(screen, LINE_COLOR, (*pos, CELL_WIDTH, CELL_HEIGHT), 2)

        # Draw the cell name, breaking text into multiple lines if necessary
        words = name.split()
        lines = []
        current_line = words[0]
        
        for word in words[1:]:
            test_line = current_line + " " + word
            if font.size(test_line)[0] > CELL_WIDTH - 10:
                lines.append(current_line)
                current_line = word
            else:
                current_line = test_line
        lines.append(current_line)
        
        # Render each line of text
        y_offset = (CELL_HEIGHT - len(lines) * font.get_height()) / 2
        for line in lines:
            text = font.render(line, True, LINE_COLOR)
            text_rect = text.get_rect(center=(pos[0] + CELL_WIDTH / 2, pos[1] + y_offset + font.get_height() / 2))
            screen.blit(text, text_rect)
            y_offset += font.get_height()

# Initialize player
player_pos = 0
player_color = (0, 0, 255)  # Red color for the player token

def draw_player():
    player_pixel_pos = pixel_positions[player_pos]
    # Draw the black outline circle
    pygame.draw.circle(screen, BLACK, (player_pixel_pos[0] + CELL_WIDTH // 2, player_pixel_pos[1] + CELL_HEIGHT // 2), CELL_WIDTH // 4 + 2)
    # Draw the player circle
    pygame.draw.circle(screen, player_color, (player_pixel_pos[0] + CELL_WIDTH // 2, player_pixel_pos[1] + CELL_HEIGHT // 2), CELL_WIDTH // 4)

def move_player(steps):
    global player_pos
    player_pos = (player_pos + steps) % len(pixel_positions)

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    dice_value, dice1, dice2 = dice_roll()
                    draw_board()
                    display_dice(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                    pygame.display.update()
                    time.sleep(1)  # Delay before moving the player
                    move_player(dice_value)

        draw_board()
        draw_player()
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
