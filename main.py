from window import Window, Line, Point

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(50,50), Point(400,400)), "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()