import pygame
import sys

pygame.init()

FPS = 60
ROWS = 6
COLS = 7
CIRCLE_RADIUS = 40
CELL_SIZE = 100
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
WINDOW_SIZE = (WIDTH, HEIGHT)

BG_COLOR = (30, 30, 60)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (200, 200, 200)

board = [[0 for _ in range(COLS)] for _ in range(ROWS)]

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Connect 4")
clock = pygame.time.Clock()

def draw_board():
    screen.fill(BG_COLOR)
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE + CELL_SIZE // 2
            y = row * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.circle(screen, CIRCLE_COLOR, (x, y), CIRCLE_RADIUS)
    pygame.display.update()

def get_column_from_click(pos):
    x, _ = pos
    col = x // CELL_SIZE
    return col

def drop_piece(board, col, player):
    for row in reversed(range(ROWS)):
        

        

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = get_column_from_click(pos)
            print(f"Clicked on column: {col}")
    
    draw_board()

pygame.quit()
sys.exit()





