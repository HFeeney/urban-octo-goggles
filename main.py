import pygame as pg
import time
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

    def new(self):
        # start a new game
        self.puzzle = Puzzle(0, 0, WIDTH)
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
            self.draw()
            self.playing = False
            time.sleep(3)
            

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

    def draw_font(self, text, size, color, x, y):
        font = pg.font.SysFont("garamond", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BLUE)
        self.draw_font("Use arrow keys", 50, WHITE, WIDTH / 2, HEIGHT / 2 - 50)
        self.draw_font("to solve puzzle", 50, WHITE, WIDTH / 2, HEIGHT / 2 + 50)
        pg.display.flip()
        self.await_key_press()
        
    def await_key_press(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    waiting = False

    def show_go_screen(self):
        if not self.running:
            return
        self.screen.fill(BLUE)
        self.draw_font("You win!", 50, WHITE, WIDTH / 2, HEIGHT / 2 - 50)
        self.draw_font("Press a key to play again", 50, WHITE, WIDTH / 2, HEIGHT / 2 + 50)
        pg.display.flip()
        self.await_key_press()

g = Game()
while g.running:
    g.show_start_screen()
    g.new()
    g.show_go_screen()

pg.quit()