import pygame as pg
from settings import *
from classes import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.puzzle = Puzzle(0, 0, WIDTH)

    def new(self):
        # start a new game
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        if (self.puzzle.check_solved()):
            self.playing = False

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.puzzle.move("UP")
                elif event.key == pg.K_DOWN:
                    self.puzzle.move("DOWN")
                elif event.key == pg.K_LEFT:
                    self.puzzle.move("LEFT")
                elif event.key == pg.K_RIGHT:
                    self.puzzle.move("RIGHT")

    def draw(self):
        # Game Loop - draw
        self.screen.fill(WHITE)
        self.puzzle.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        print("START")

    def show_go_screen(self):
        # game over/continue
        print("SOLVED")
        self.running = False

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()