import random
from Settings import BLOCKS, BLOCK_COLOURS
import View


class Block(object):
    NUMBER_ROWS = 20
    NUMBER_COLUMNS = 10

    def __init__(self, x, y, block):
        self.x = x
        self.y = y
        self.block = block
        self.color = BLOCK_COLOURS[BLOCKS.index(block)]
        self.orientation = 0


def createGrid(staticBlocks=None):
    if staticBlocks is None:
        staticBlocks = {}
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if (column, row) in staticBlocks:
                key = staticBlocks[(column, row)]
                grid[row][column] = key
    return grid


def changeBlockFormat(block):
    positions = []
    format = block.block[block.orientation % len(block.block)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '*':
                positions.append((block.x + j, block.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def inValidRegion(block, grid):
    validPositions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    validPositions = [j for sub in validPositions for j in sub]
    formatted = changeBlockFormat(block)

    for position in formatted:
        if position not in validPositions:
            if position[1] > -1:
                return False

    return True


def isOverScreen(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def getShape():
    return Block(5, 0, random.choice(BLOCKS))


def clearRows(grid, static):
    View.clearRows(grid, static)


def drawWindow(surface, grid):
    View.drawWindow(surface, grid)


def drawNextBlock(block, surface, score):
    View.drawNextBlock(block, surface, score)


def drawTextMiddle(text, size, color, surface):
    View.drawTextMiddle(text, size, color, surface)
