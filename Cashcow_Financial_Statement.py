import pygame
import sys

pygame.init()

screen_width = 500
screen_height = 1000

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("financial Statement")

font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(WHITE)

    draw_text("Financial Statement", font, BLACK, screen, 20, 20)
    draw_text("Income", font, BLACK, screen, 20, 80)
    pygame.draw.line(screen, BLACK, (20, 120), (screen_width - 20, 120), 2)
    draw_text("Description", small_font, BLACK, screen, 40, 140)
    draw_text("Cash Flow", small_font, BLACK, screen, 500, 140)

    income_items = ["Salary:", "Interest/Dividends:", "Real Estate/Business:"]
    y_offset = 180
    for item in income_items:
        draw_text(item, small_font, BLACK, screen, 40, y_offset)
        y_offset +=40

    draw_text("Expenses", font, BLACK, screen, 20, 300)
    pygame.draw.line(screen, BLACK, (20, 340), (screen_width - 20, 340), 2)
    expenses_items = ["Taxes:", "Home Mortgage Payment:", "School Loan Payment:", "Car Loan Payment:", "Credit Card Payment:", "Other Expenses:", "Bank Loan Payment:", "Per Child Expenses:"]
    y_offset = 360
    for item in expenses_items:
        draw_text(item, small_font, BLACK, screen, 40, y_offset)
        y_offset +=40

    draw_text("Assets", font, BLACK, screen, 20, 640)
    pygame.draw.line(screen, BLACK, (20, 680), (screen_width - 20, 680), 2)
    assets_items = ["Savings:", "Precious Metals/ Etc.:", "Stocks/Funds/CDs:", "Real Estate/Business:"]
    y_offset = 700
    for item in assets_items:
        draw_text(item, small_font, BLACK, screen, 40, y_offset)
        y_offset +=40

    draw_text("Liabilities", font, BLACK, screen, 20, 860)
    pygame.draw.line(screen, BLACK, (20, 900), (screen_width - 20, 900), 2)
    assets_items = ["Home Mortgage:", "School Loans:", "Car Loans:", "Credit Card Debt:", "Card Debt", "Bank Loan:", "Real Estate/Business:"]
    y_offset = 920
    for item in assets_items:
        draw_text(item, small_font, BLACK, screen, 40, y_offset)
        y_offset +=40

    draw_text("Profession", small_font, BLACK, screen, 600, 80)
    pygame.draw.rect(screen, BLACK, (600, 120, 180, 40), 2)
    draw_text("Dream", small_font, BLACK, screen, 600, 180)
    pygame.draw.rect(screen, BLACK, (600, 220, 180, 40), 2)
    draw_text("Auditor", small_font, BLACK, screen, 600, 280)
    pygame.draw.rect(screen, BLACK, (600, 320, 180, 40), 2)

    pygame.draw.rect(screen, BLACK, (600, 400, 180, 40), 2) # Salary Box
    pygame.draw.rect(screen, BLACK, (600, 460, 180, 40), 2) # Passive Income Box
    pygame.draw.rect(screen, BLACK, (600, 520, 180, 40), 2) # Total Income Box
    pygame.draw.rect(screen, BLACK, (600, 580, 180, 40), 2) # Total Expenses Box

    pygame.display.flip()