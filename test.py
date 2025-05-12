import unittest
from maze import Maze
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
    
    def test_maze_entrance_open(self):
        m1 = Maze(0,0,10,10,10,10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
    
    def test_maze_exit_open(self):
        m1 = Maze(0,0,10,10,10,10)
        self.assertEqual(
            m1._cells[m1.num_rows - 1][m1.num_cols - 1].has_bottom_wall,
            False
        )
    
    def test_maze_break_wall(self):
        m1 = Maze(0,0,10,10,10,10,seed=0)
        self.assertEqual(
            m1._cells[3][5].has_bottom_wall,
            False
        )
        self.assertEqual(
            m1._cells[3][5].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[3][5].has_left_wall,
            False
        )
        self.assertEqual(
            m1._cells[3][5].has_right_wall,
            False
        )
    
    def test_reset_visit(self):
        m1 = Maze(0,0,10,10,10,10,seed=0)
        self.assertEqual(
            m1._cells[0][0].visited,
            False
        )





if __name__ == "__main__":
    unittest.main()