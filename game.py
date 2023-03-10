import pygame
import config
from player import Player


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
        self.player = Player(self)
        self.all_sprites = pygame.sprite.Group()

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

    def draw(self):
        pass

    def quit(self):
        pygame.quit()
        quit()
