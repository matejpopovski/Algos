import pygame
import sys

pygame.init()

# Game settings
FPS = 60
ROWS = 6
COLS = 7
CIRCLE_RADIUS = 40
CELL_SIZE = 100
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
WINDOW_SIZE = (WIDTH, HEIGHT)

# Colors
BG_COLOR = (30, 30, 60)
CIRCLE_COLOR = (200, 200, 200)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LINE_COLOR = (255, 255, 255)

# Fonts
font = pygame.font.SysFont("Arial", 48)

# Game state
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
current_player = 1
winner = 0
winning_coords = []
game_over = False

# Pygame setup
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
                color = RED
            elif board[row][col] == 2:
                color = YELLOW

            pygame.draw.circle(screen, color, (x, y), CIRCLE_RADIUS)

    # Draw winning line if any
    if winning_coords:
        (r1, c1), (r2, c2) = winning_coords[0], winning_coords[-1]
        x1 = c1 * CELL_SIZE + CELL_SIZE // 2
        y1 = r1 * CELL_SIZE + CELL_SIZE // 2
        x2 = c2 * CELL_SIZE + CELL_SIZE // 2
        y2 = r2 * CELL_SIZE + CELL_SIZE // 2
        color = RED if winner == 1 else YELLOW
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), 8)

    pygame.display.update()

def get_column_from_click(pos):
    x, _ = pos
    return x // CELL_SIZE

def drop_piece(board, col, player):
    for row in reversed(range(ROWS)):
        if board[row][col] == 0:
            board[row][col] = player
            return True
    return False

def define_winner(board):
    directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]  # ↓, →, ↘, ↗
    for row in range(ROWS):
        for col in range(COLS):
            player = board[row][col]
            if player == 0:
                continue

            for dr, dc in directions:
                coords = []
                for i in range(4):
                    r = row + dr * i
                    c = col + dc * i
                    if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
                        coords.append((r, c))
                    else:
                        break
                if len(coords) == 4:
                    return player, coords
    return 0, []

def display_message(text, color):
    msg = font.render(text, True, color)
    msg_rect = msg.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(msg, msg_rect)
    pygame.display.update()

# Main game loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            col = get_column_from_click(pos)
            if drop_piece(board, col, current_player):
                winner, winning_coords = define_winner(board)
                if winner != 0:
                    game_over = True
                current_player = 2 if current_player == 1 else 1

    draw_board()

    if game_over:
        display_message(f"Player {winner} wins!", RED if winner == 1 else YELLOW)
        pygame.time.wait(3000)
        running = False

pygame.quit()
sys.exit()
