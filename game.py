import pygame
import config
from board import Board


# create a new game object using pygame
# use config for constants

class Game:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = config.SCREEN_WIDTH, config.SCREEN_HEIGHT
        self.display = pygame.display.set_mode(self.size)
        self.caption = config.TITLE
        self.clock = pygame.time.Clock()
        self.fps = config.FPS
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.board = Board()


    def run(self):
        while self.running:
            self.clock.tick(self.fps)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()
        self.board.add_block()

    def draw(self):
        self.display.fill(config.BLACK)
        self.board.draw(self.display)
        self.all_sprites.draw(self.display)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        quit()
