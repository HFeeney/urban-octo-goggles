import pygame as pg

class Puzzle:
    def __init__(self, x, y, side):
        self.surface = pg.Surface((side, side))        
        self.image = pg.image.load("Final Design.jpg")
        self.surface.blit(self.image, (0, 0))
        self.side = side
        self.rect = self.surface.get_rect()
        self.rect.topleft = (x, y)
        self.tiles = [[0]*3]*3
        for i in range(3):
            for j in range(3):
                self.tiles[i][j] = pg.Surface((self.side / 3, self.side / 3))
                self.tiles[i][j].blit(self.image, (0, 0), (self.side / 3 * i, self.side / 3 * j, self.side / 3, self.side / 3))

    def draw(self):
        pass

