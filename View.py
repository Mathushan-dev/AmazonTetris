import pygame

from Settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TOP_LEFT_X, \
    SCREEN_TOP_LEFT_Y


def drawTextMiddle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, True, color)

    surface.blit(label, (SCREEN_TOP_LEFT_X + SCREEN_WIDTH / 2 - (label.get_width() / 2),
                         SCREEN_TOP_LEFT_Y + SCREEN_HEIGHT / 2 - label.get_height() / 2))


def drawGrid(surface, row, col):
    sx = SCREEN_TOP_LEFT_X
    sy = SCREEN_TOP_LEFT_Y
    for i in range(row):
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * 30),
                         (sx + SCREEN_WIDTH, sy + i * 30))
        for j in range(col):
            pygame.draw.line(surface, (128, 128, 128), (sx + j * 30, sy),
                             (sx + j * 30, sy + SCREEN_HEIGHT))


def clearRows(grid, static):
    inc = 0
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del static[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(static), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                static[newKey] = static.pop(key)


def drawNextBlock(shape, surface, score):
    font = pygame.font.SysFont('comicsans', 30)
    nextLabel = font.render('Next Shape', True, (0, 214, 188))
    scoreLabel = font.render('Score', True, (0, 214, 188))
    score = font.render(str(score), True, (0, 214, 188))

    sx = SCREEN_TOP_LEFT_X + SCREEN_WIDTH + 50
    sy = SCREEN_TOP_LEFT_Y + SCREEN_HEIGHT / 2 - 100
    format = shape.block[shape.orientation % len(shape.block)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '*':
                pygame.draw.rect(surface, shape.color, (sx + j * 30, sy + i * 30, 30, 30), 0)

    surface.blit(nextLabel, (sx + 10, sy - 30))
    surface.blit(scoreLabel, (sx + 10, sy + 150))
    surface.blit(score, (sx + 10, sy + 170))


def drawWindow(surface, grid):
    surface.fill((0, 0, 0))
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('TETRIS', True, (0, 214, 188))

    surface.blit(label, (SCREEN_TOP_LEFT_X + SCREEN_WIDTH / 2 - (label.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (SCREEN_TOP_LEFT_X + j * 30, SCREEN_TOP_LEFT_Y + i * 30, 30, 30), 0)

    drawGrid(surface, 20, 10)
    pygame.draw.rect(surface, (0, 214, 188), (SCREEN_TOP_LEFT_X, SCREEN_TOP_LEFT_Y, SCREEN_WIDTH, SCREEN_HEIGHT), 5)
