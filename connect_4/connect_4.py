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

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Connect 4")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(f"Mouse clicked at: {pos}")
    
    screen.fill((30, 30, 60))
    
    pygame.display.flip()

pygame.quit()
sys.exit()





