import pygame
import config
from block import Block


# create board object which will house the blocks
# board will be in center of screen
# board will be a 2d array of blocks
# board will be 10x20, border drawn on screen
# board will be drawn on the screen
# board will check for collisions
# board will check for full rows
# board will add blocks to the board


class Board:
    def __init__(self):
        self.board = [[0 for x in range(config.BOARD_WIDTH)] for y in range(config.BOARD_HEIGHT)]
        self.active_block = None

    def draw(self, display):
        # draw even horizontal and vertical grid lines on board for easier block placement
        # use block size for grid lines
        # draw blocks on board
        for x in range(0, config.BOARD_WIDTH, config.BLOCK_SIZE):
            for y in range(0, config.BOARD_HEIGHT, config.BLOCK_SIZE):
                rect = pygame.Rect(x, y, config.BLOCK_SIZE, config.BLOCK_SIZE)
                rect.center = (config.SCREEN_WIDTH // 2 - config.BOARD_WIDTH // 2 + x,
                               config.SCREEN_HEIGHT // 2 - config.BOARD_HEIGHT // 2 + y)
                pygame.draw.rect(display, config.WHITE, rect, 1)
        for y in range(20):
            for x in range(10):
                if self.board[y][x] != 0:
                    self.board[y][x].draw(display)

    # add block to board, block needs to be initially placed at top middle of board grid
    #
    def add_block(self):
        if self.active_block is None:
            block = Block(config.BOARD_WIDTH // 2 - config.BLOCK_SIZE // 2, 0)
            self.active_block = block
        else:
            if self.check_collision(self.active_block):
                self.board[self.active_block.rect.y // 20][self.active_block.rect.x // 20] = self.active_block
                self.active_block = None
            else:
                self.active_block.rect.y += 5

    def check_row(self):
        for y in range(20):
            if 0 not in self.board[y]:
                self.board.pop(y)
                self.board.insert(0, [0 for x in range(10)])

    def check_collision(self, block):
        if block.rect.y // 20 == 19:
            return True
        elif self.board[block.rect.y // 20 + 1][block.rect.x // 20] != 0:
            return True
        else:
            return False
