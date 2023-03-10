import pygame
import config
import random


# block object for tetris blocks
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((config.BLOCK_SIZE, config.BLOCK_SIZE))
        self.random_block()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # random block generator. each block has a different color using config colors
    # each block has a different shape
    def random_block(self):
        block = random.randint(0, 6)
        if block == 0:
            self.image.fill(config.BLUE)
        elif block == 1:
            self.image.fill(config.GREEN)
        elif block == 2:
            self.image.fill(config.RED)
        elif block == 3:
            self.image.fill(config.YELLOW)
        elif block == 4:
            self.image.fill(config.PURPLE)
        elif block == 5:
            self.image.fill(config.ORANGE)
        elif block == 6:
            self.image.fill(config.CYAN)

    def draw(self, display):
        display.blit(self.image, self.rect)
