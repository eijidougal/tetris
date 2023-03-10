import pygame


# create a new game object using pygame

class Game:
    def __init__(self):
        self.running = True
        self.playing = False
        self.display = None
        self.size = self.width, self.height = 800, 600
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.caption = "Tetris"
        self.player = None
        self.all_sprites = None

    def new(self):
        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)
        self.playing = True
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)

    def run(self):
        while self.playing:
            self.clock.tick(self.fps)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        pass

    def quit(self):
        pygame.quit()
        quit()
