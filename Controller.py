import pygame
from Model import createGrid, changeBlockFormat, inValidRegion, isOverScreen, getShape, clearRows, drawWindow, drawNextBlock, drawTextMiddle
from Settings import CANVAS_WIDTH, CANVAS_HEIGHT


def main():
    global grid

    staticBlocks = {}
    grid = createGrid(staticBlocks)

    changeBlock = False
    run = True
    currentBlock = getShape()
    nextBlock = getShape()
    clock = pygame.time.Clock()
    fallTime = 0
    score = 0

    while run:
        fallSpeed = 0.27

        grid = createGrid(staticBlocks)
        fallTime += clock.get_rawtime()
        clock.tick()

        if fallTime / 1000 >= fallSpeed:
            fallTime = 0
            currentBlock.y += 1
            if not (inValidRegion(currentBlock, grid)) and currentBlock.y > 0:
                currentBlock.y -= 1
                changeBlock = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    currentBlock.x -= 1
                    if not inValidRegion(currentBlock, grid):
                        currentBlock.x += 1

                elif event.key == pygame.K_RIGHT:
                    currentBlock.x += 1
                    if not inValidRegion(currentBlock, grid):
                        currentBlock.x -= 1

                elif event.key == pygame.K_UP:
                    currentBlock.orientation = currentBlock.orientation + 1 % len(currentBlock.block)
                    if not inValidRegion(currentBlock, grid):
                        currentBlock.orientation = currentBlock.orientation - 1 % len(currentBlock.block)

                if event.key == pygame.K_DOWN:
                    currentBlock.y += 1
                    if not inValidRegion(currentBlock, grid):
                        currentBlock.y -= 1

        shapePosition = changeBlockFormat(currentBlock)

        for i in range(len(shapePosition)):
            x, y = shapePosition[i]
            if y > -1:
                grid[y][x] = currentBlock.color

        if changeBlock:
            for position in shapePosition:
                key = (position[0], position[1])
                staticBlocks[key] = currentBlock.color
            currentBlock = nextBlock
            nextBlock = getShape()
            score += 10
            changeBlock = False

            clearRows(grid, staticBlocks)

        drawWindow(win, grid)
        drawNextBlock(nextBlock, win, score)
        pygame.display.update()

        if isOverScreen(staticBlocks):
            run = False

    drawTextMiddle("Game Over - Score " + str(score), 70, (255, 255, 255), win)
    pygame.display.update()
    pygame.time.delay(2000)


def main_menu():
    run = True
    while run:
        win.fill((0, 0, 0))
        drawTextMiddle('Enter', 60, (255, 153, 0), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()


if __name__ == "__main__":
    pygame.font.init()

    win = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    pygame.display.set_caption('Tetris')

    main_menu()
