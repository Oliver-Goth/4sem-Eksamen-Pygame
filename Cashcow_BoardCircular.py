import pygame
import sys
import math
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

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Circular Track")

# Define the positions for the circular track
def generate_circular_positions(center_x, center_y, radius, num_cells):
    angle_step = 2 * math.pi / num_cells
    return [
        (
            int(center_x + radius * math.cos(i * angle_step) - CELL_WIDTH // 2),
            int(center_y + radius * math.sin(i * angle_step) - CELL_HEIGHT // 2)
        )
        for i in range(num_cells)
    ]

# Center and radius for the circular track
center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
radius = 3 * CELL_WIDTH

# Define the circular track cell positions
circular_positions = generate_circular_positions(center_x, center_y, radius, 12)

# Cell data for the circular track
circular_cell_data = [
    ("Payday", BLUE),
    ("Real Estate Deal", GREEN),
    ("Market Crash", RED),
    ("Startup Success", GREEN),
    ("Tax Refund", YELLOW),
    ("New Car", RED),
    ("Stock Dividend", GREEN),
    ("Business Expansion", BLUE),
    ("Legal Fees", RED),
    ("Lottery Win", YELLOW),
    ("Medical Bills", RED),
    ("New Equipment", GREEN)
]

def draw_circular_track():
    screen.fill(BOARD_COLOR)
    font = pygame.font.SysFont(None, 24)
    
    for idx, pos in enumerate(circular_positions):
        name, color = circular_cell_data[idx]
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
player_color = (0, 0, 255)  # Blue color for the player token

def draw_player():
    player_pixel_pos = circular_positions[player_pos]
    # Draw the black outline circle
    pygame.draw.circle(screen, BLACK, (player_pixel_pos[0] + CELL_WIDTH // 2, player_pixel_pos[1] + CELL_HEIGHT // 2), CELL_WIDTH // 4 + 2)
    # Draw the player circle
    pygame.draw.circle(screen, player_color, (player_pixel_pos[0] + CELL_WIDTH // 2, player_pixel_pos[1] + CELL_HEIGHT // 2), CELL_WIDTH // 4)

def move_player(steps):
    global player_pos
    player_pos = (player_pos + steps) % len(circular_positions)

def main():
    clock = pygame.time.Clock()

    # Initial roll to display the dice
    dice_value, dice1 = dice_roll()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Roll the dice when 'r' is pressed
                    dice_value, dice1 = dice_roll()
                    move_player(dice_value)

        # Redraw the board, player, and dice
        screen.fill(BOARD_COLOR)
        draw_circular_track()
        draw_player()
        display_dice(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
