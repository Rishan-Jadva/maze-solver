from window import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = False
        self.__y1 = False
        self.__x2 = False
        self.__y2 = False
        self.__win = win
    
    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line)
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line)
        
    def draw_move(self, to_cell, undo=False):
        len_x = max(self.__x1, self.__x2) - min(self.__x1, self.__x2)
        len_y = max(self.__y1, self.__y2) - min(self.__y1, self.__y2)
        x_center = len_x // 2 + min(self.__x1, self.__x2)
        y_center = len_y // 2 + min(self.__y1, self.__y2)

        len_x2 = max(to_cell.__x1, to_cell.__x2) - min(to_cell.__x1, to_cell.__x2)
        len_y2 = max(to_cell.__y1, to_cell.__y2) - min(to_cell.__y1, to_cell.__y2)
        x_center2 = len_x2 // 2 + min(to_cell.__x1, to_cell.__x2)
        y_center2 = len_y2 // 2 + min(to_cell.__y1, to_cell.__y2)

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))

        if undo:
            color = "gray"
        else:
            color = "red"

        self.__win.draw_line(line, color)
