from collections import namedtuple


class Point(namedtuple("Point", "x y", defaults=[0, 0])):
    """
    Class to store points
    """
    def __repr__(self):
        return f"Point: x = {self.x}, y = {self.y}"
