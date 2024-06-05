import unittest
from maze import maze
from graphics import*

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = window(width=500, height=500)
        num_cols = 12
        num_rows = 10
        m1 = maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )


if __name__ == "__main__":
    unittest.main()
