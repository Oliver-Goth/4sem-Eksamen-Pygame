import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1500, 1000
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 50
MENU_WIDTH, MENU_HEIGHT = 300, SCREEN_HEIGHT
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (220, 220, 220)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cashcow Menu")

# Font setup
font = pygame.font.SysFont(None, 36)

def draw_button():
    pygame.draw.rect(screen, GRAY, (0, 0, BUTTON_WIDTH, BUTTON_HEIGHT))
    text = font.render("Menu", True, BLACK)
    text_rect = text.get_rect(center=(BUTTON_WIDTH // 2, BUTTON_HEIGHT // 2))
    screen.blit(text, text_rect)

def draw_menu():
    pygame.draw.rect(screen, LIGHT_GRAY, (0, 0, MENU_WIDTH, MENU_HEIGHT))
    menu_items = ["Item 1", "Item 2", "Item 3", "Item 4"]
    for idx, item in enumerate(menu_items):
        text = font.render(item, True, BLACK)
        text_rect = text.get_rect(topleft=(10, 10 + idx * 40))
        screen.blit(text, text_rect)

def main():
    clock = pygame.time.Clock()
    menu_open = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if 0 <= mouse_pos[0] <= BUTTON_WIDTH and 0 <= mouse_pos[1] <= BUTTON_HEIGHT:
                        menu_open = not menu_open

        screen.fill(WHITE)
        draw_button()
        if menu_open:
            draw_menu()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
