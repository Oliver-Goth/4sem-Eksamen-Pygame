import pygame
import random

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 24

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cashcow Economics")

# Fonts
font = pygame.font.SysFont(None, FONT_SIZE)

# Classes
class Income:
    def __init__(self, description, cashflow):
        self.description = description
        self.cashflow = cashflow

    def display(self, x, y):
        text = font.render(f"{self.description}: ${self.cash}", True, BLACK)
        screen.blit(text, (x, y))

class Expenses:
    def __init__(self, description, cashflow):
        self.description = description
        self.cashflow = cashflow

    def display(self, x, y):
        text = font.render(f"{self.description}: ${self.cash}", True, BLACK)
        screen.blit(text, (x, y))

class Assets:
    def __init__(self, description, cashflow):
        self.description = description
        self.cashflow = cashflow

    def display(self, x, y):
        text = font.render(f"{self.description}: ${self.cash}", True, BLACK)
        screen.blit(text, (x, y))

class Liabilities:
    def __init__(self, description, cashflow):
        self.description = description
        self.cashflow = cashflow

    def display(self, x, y):
        text = font.render(f"{self.description}: ${self.cash}", True, BLACK)
        screen.blit(text, (x, y))