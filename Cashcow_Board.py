import pygame
import sys
import math
from Cashcow_Dice import dice_roll, display_dice

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1500, 1000
CELL_WIDTH, CELL_HEIGHT = 100, 100
BOARD_COLOR = (255, 245, 196)
LINE_COLOR = (0, 0, 0)
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 215, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

rolling_audio = pygame.mixer.Sound('audio/roll_audio.mp3')
rolling_stop_audio = pygame.mixer.Sound('audio/roll_stop_audio.mp3')

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

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Board game")

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

board_width = 13 * CELL_WIDTH
board_height = 9 * CELL_HEIGHT
start_x = (SCREEN_WIDTH - board_width) // 2
start_y = (SCREEN_HEIGHT - board_height) // 2

rectangular_positions = [(start_x + x * CELL_WIDTH, start_y + y * CELL_HEIGHT) for x, y in cell_positions]

def generate_circular_positions(center_x, center_y, radius, num_cells):
    angle_step = 2 * math.pi / num_cells
    return [
        (
            int(center_x + radius * math.cos(i * angle_step) - CELL_WIDTH // 2),
            int(center_y + radius * math.sin(i * angle_step) - CELL_HEIGHT // 2)
        )
        for i in range(num_cells)
    ]

center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
radius = 3 * CELL_WIDTH

circular_positions = generate_circular_positions(center_x, center_y, radius, 20)

circular_cell_data = [
    ("Market", BLUE),
    ("Deals", GREEN),
    ("Doodad", RED),
    ("Deals", GREEN),
    ("Baby", PURPLE),
    ("Deals", GREEN),
    ("Payday", ORANGE),
    ("Deals", GREEN),
    ("Legal Fees", RED),
    ("Deals", GREEN),
    ("Market", BLUE),
    ("Deals", GREEN),
    ("Doodad", RED),
    ("Deals", GREEN),
    ("Charity", PURPLE),
    ("Deals", GREEN),
    ("Payday", ORANGE),
    ("Deals", GREEN),
    ("Legal Fees", RED),
    ("Deals", GREEN),
    ("Market", BLUE),
    ("Deals", GREEN),
    ("Doodad", RED),
    ("Deals", GREEN),
    ("Downsized", PURPLE),
    ("Deals", GREEN),
    ("Payday", ORANGE),
    ("Deals", GREEN),
    ("Legal Fees", RED),
    ("Deals", GREEN)
]

def draw_board():
    screen.fill(BOARD_COLOR)
    font = pygame.font.SysFont(None, 24)
    
    for idx, pos in enumerate(rectangular_positions):
        name, color = cell_data[idx]
        pygame.draw.rect(screen, color, (*pos, CELL_WIDTH, CELL_HEIGHT))
        pygame.draw.rect(screen, LINE_COLOR, (*pos, CELL_WIDTH, CELL_HEIGHT), 2)

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
        
        y_offset = (CELL_HEIGHT - len(lines) * font.get_height()) / 2
        for line in lines:
            text = font.render(line, True, LINE_COLOR)
            text_rect = text.get_rect(center=(pos[0] + CELL_WIDTH / 2, pos[1] + y_offset + font.get_height() / 2))
            screen.blit(text, text_rect)
            y_offset += font.get_height()

    for idx, pos in enumerate(circular_positions):
        name, color = circular_cell_data[idx]
        pygame.draw.rect(screen, color, (*pos, CELL_WIDTH, CELL_HEIGHT))
        pygame.draw.rect(screen, LINE_COLOR, (*pos, CELL_WIDTH, CELL_HEIGHT), 2)

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
        
        y_offset = (CELL_HEIGHT - len(lines) * font.get_height()) / 2
        for line in lines:
            text = font.render(line, True, LINE_COLOR)
            text_rect = text.get_rect(center=(pos[0] + CELL_WIDTH / 2, pos[1] + y_offset + font.get_height() / 2))
            screen.blit(text, text_rect)
            y_offset += font.get_height()

player_pos = 0
player_track = 'circular'
player_color = (0, 0, 255)

def draw_player():
    if player_track == 'circular':
        player_rectangular_pos = circular_positions[player_pos]
    else:
        player_rectangular_pos = rectangular_positions[player_pos]
        
    pygame.draw.circle(screen, BLACK, (player_rectangular_pos[0] + CELL_WIDTH // 2, player_rectangular_pos[1] + CELL_HEIGHT // 2), CELL_WIDTH // 4 + 2)
    pygame.draw.circle(screen, player_color, (player_rectangular_pos[0] + CELL_WIDTH // 2, player_rectangular_pos[1] + CELL_HEIGHT // 2), CELL_WIDTH // 4)

def move_player(steps):
    global player_pos, player_track
    
    if player_track == 'circular':
        player_pos = (player_pos + steps) % len(circular_positions)
    else:
        player_pos = (player_pos + steps) % len(rectangular_positions)

def draw_button(surface, color, rect):
    pygame.draw.rect(surface, color, rect)

def animated_dice_roll():
    rolling_audio.play()
    for e in range(15):
        dice_value = dice_roll()[0]
        screen.fill(BOARD_COLOR)
        draw_board()
        draw_player()
        display_dice(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.display.flip()
        pygame.time.delay(30)
    rolling_stop_audio.play()

def main():
    global player_track
    
    clock = pygame.time.Clock()

    dice_value, dice1 = dice_roll()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    animated_dice_roll()
                    dice_value, dice1 = dice_roll()
                    move_player(dice_value)
                if event.key == pygame.K_t:
                    if player_track == 'rectangular':
                        player_pos = 0
                        player_track = 'circular'
                    elif player_track == 'circular':
                        player_pos = 0
                        player_track = 'rectangular'
                        
        screen.fill(BOARD_COLOR)
        draw_board()
        draw_player()
        display_dice(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
