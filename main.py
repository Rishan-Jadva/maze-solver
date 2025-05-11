from window import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    c = Cell(win)
    c.has_right_wall = False
    c.draw(100, 200, 300, 400)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.draw(300, 200, 500, 400)

    c.draw_move(c2)

    win.wait_for_close()

if __name__ == "__main__":
    main()