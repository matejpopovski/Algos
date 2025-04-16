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
current_player = 1 

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Connect 4")
clock = pygame.time.Clock()

def draw_board():
    screen.fill(BG_COLOR)
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE + CELL_SIZE // 2
            y = row * CELL_SIZE + CELL_SIZE // 2
            
            if board[row][col] == 0:
                color = CIRCLE_COLOR
            elif board[row][col] == 1:
                color = (255, 0, 0)  # Red
            elif board[row][col] == 2:
                color = (255, 255, 0)  # Yellow

            pygame.draw.circle(screen, color, (x, y), CIRCLE_RADIUS)
    pygame.display.update()

def get_column_from_click(pos):
    x, _ = pos
    col = x // CELL_SIZE
    return col

def drop_piece(board, col, player):
    for row in reversed(range(ROWS)):
        if board[row][col] == 0:
            board[row][col] = player
            return True
    return False

def define_winner(board):
    for row in range(ROWS):
        for col in range(COLS):
            player = board[row][col]
            if player == 0:
                continue 

            if row + 3 < ROWS:
                if all(board[row + i][col] == player for i in range(4)):
                    return player

            if col + 3 < COLS:
                if all(board[row][col + i] == player for i in range(4)):
                    return player

            if row + 3 < ROWS and col + 3 < COLS:
                if all(board[row + i][col + i] == player for i in range(4)):
                    return player

            if row - 3 >= 0 and col + 3 < COLS:
                if all(board[row - i][col + i] == player for i in range(4)):
                    return player

    return 0 

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
            if drop_piece(board, col, current_player):
                current_player = 2 if current_player == 1 else 1
    
    draw_board()
    winner = define_winner(board, winner)
    if winner != 0:
        print(f"Player {winner} wins!")
        pygame.quit()
        sys.exit()

pygame.quit()
sys.exit()



