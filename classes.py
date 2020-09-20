import pygame as pg
import random
from settings import * 

class Puzzle:
    def __init__(self, x, y, side):
        self.surface = pg.Surface((side, side))        
        self.image = pg.transform.scale(pg.image.load("Final Design.jpg").convert(), (WIDTH, HEIGHT))
        self.surface.blit(self.image, (0, 0))
        self.side = side
        self.rect = self.surface.get_rect()
        self.rect.topleft = (x, y)
        self.tiles = [0]*9
        self.positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.empty_tile_index = 8
        for i in range(3):
            for j in range(3):
                self.tiles[i * 3 + j] = pg.Surface((self.side / 3, self.side / 3))
                if (i == 2 and j == 2):
                    self.tiles[8].fill(WHITE)
                else:
                    self.tiles[i * 3 + j].blit(self.image, (0, 0), (self.side / 3 * j, self.side / 3 * i, self.side / 3, self.side / 3))
        self.shuffle_tiles()

    def check_solvable(self, arr):
        inversions = 0
        for i in range(7):
            for j in range(i + 1, 8):
                if (arr[i] > arr[j]):
                    inversions += 1
        if (inversions % 2 == 0):
            return True
        return False
    
    def check_solved(self):
        check = 0
        for item in self.positions:
            if (item != check):
                return False
            check += 1
        return True

    def shuffle_tiles(self):
        self.positions.pop(8)
        random.shuffle(self.positions)
        while (self.check_solvable(self.positions) != True or self.check_solved()):
            random.shuffle(self.positions)
        self.positions.append(8)

    def swap_tiles(self, pos1, pos2):
        p1 = self.positions.pop(pos1)
        p2 = self.positions.pop(pos2 - 1)
        self.positions.insert(pos1, p2)
        self.positions.insert(pos2, p1)

    def move(self, direction):
        if (direction == "UP"):
            if (self.empty_tile_index + 3 <= 8):
                self.swap_tiles(self.empty_tile_index, self.empty_tile_index + 3)
                self.empty_tile_index += 3
        elif (direction == "DOWN"):
            if (self.empty_tile_index - 3 >= 0):
                self.swap_tiles(self.empty_tile_index - 3, self.empty_tile_index)
                self.empty_tile_index -= 3
        elif (direction == "LEFT"):
            if ((self.empty_tile_index + 1) % 3 != 0):
                self.swap_tiles(self.empty_tile_index, self.empty_tile_index + 1)
                self.empty_tile_index += 1
        elif (direction == "RIGHT"):
            if (self.empty_tile_index % 3 != 0):
                self.swap_tiles(self.empty_tile_index - 1, self.empty_tile_index)
                self.empty_tile_index -= 1

    def draw(self, Surface):
        for i in range(3):
            Surface.blit(self.tiles[self.positions[i]], (i * WIDTH / 3, 0))
        for i in range(3, 6):
            Surface.blit(self.tiles[self.positions[i]], ((i - 3) * WIDTH / 3, HEIGHT / 3))
        for i in range(6, 9):
            Surface.blit(self.tiles[self.positions[i]], ((i - 6) * WIDTH / 3, HEIGHT * 2 / 3))

 