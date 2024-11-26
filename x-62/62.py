from graphics import *
import random
import time

class Cell:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.alive = False
        self.rectangle = Rectangle(Point(x, y), Point(x + size, y + size))
        self.rectangle.setOutline("black")
        self.rectangle.setFill("white")
    
    def draw(self, win):
        self.rectangle.draw(win)
    
    def update(self):
        if self.alive:
            self.rectangle.setFill("blue")
        else:
            self.rectangle.setFill("white")

class GameOfLife:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.cells = [[Cell(j * cell_size, i * cell_size, cell_size) for j in range(cols)] for i in range(rows)]
        self.win = GraphWin("Game Niggers", cols * cell_size, rows * cell_size)
        for row in self.cells:
            for cell in row:
                cell.alive = random.choice([True, False])
                cell.update()
                cell.draw(self.win)

    def get_neighbors(self, x, y):
        neighbors = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (i == 0 and j == 0):
                    ni = (x + i) % self.rows
                    nj = (y + j) % self.cols
                    neighbors.append(self.cells[ni][nj])
        return neighbors

    def update_cells(self):
        new_state = [[cell.alive for cell in row] for row in self.cells]

        for i in range(self.rows):
            for j in range(self.cols):
                alive_neighbors = sum(1 for neighbor in self.get_neighbors(i, j) if neighbor.alive)

                if self.cells[i][j].alive:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_state[i][j] = False
                else:
                    if alive_neighbors == 3:
                        new_state[i][j] = True

        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].alive = new_state[i][j]
                self.cells[i][j].update()

    def run(self):
        while True:
            self.update_cells()
            time.sleep(1/144)
            update(144)
game = GameOfLife(rows=15, cols=15, cell_size=20)
game.run()
