from cell import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                row.append(Cell(self.win))
            self._cells.append(row)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        left = self.x1 + (j * self.cell_size_x)
        top = self.y1 + (i * self.cell_size_y)
        right = left + self.cell_size_x
        bottom = top + self.cell_size_y

        self._cells[i][j].draw(left, top, right, bottom)
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        top_left = self._cells[0][0]
        top_left.has_top_wall = False
        self._draw_cell(0, 0)
        bottom_right = self._cells[self.num_rows - 1][self.num_cols - 1]
        bottom_right.has_bottom_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                visit.append((i - 1, j))
            if i < self.num_rows - 1 and not self._cells[i + 1][j].visited:
                visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                visit.append((i, j - 1))
            if j < self.num_cols - 1 and not self._cells[i][j + 1].visited:
                visit.append((i, j + 1))
            if len(visit) == 0:
                self._draw_cell(i, j)
                return
            
            direction = random.randrange(len(visit))
            visit_cell = visit[direction]

            if visit_cell[0] == i + 1:  # Moved DOWN
                self._cells[i][j].has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False
            elif visit_cell[0] == i - 1:  # Moved UP
                self._cells[i][j].has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False
            elif visit_cell[1] == j + 1:  # Moved RIGHT
                self._cells[i][j].has_right_wall = False
                self._cells[i][j + 1].has_left_wall = False
            elif visit_cell[1] == j - 1:  # Moved LEFT
                self._cells[i][j].has_left_wall = False
                self._cells[i][j - 1].has_right_wall = False

            
            self._break_walls_r(visit_cell[0],visit_cell[1])