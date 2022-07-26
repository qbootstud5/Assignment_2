from collections import namedtuple


class Color(namedtuple("Color", "red green blue", defaults=[0, 0, 0])):
    """
    Class to store the color
    """
    def __repr__(self):
        return f"Color: red = {self.red}, green = {self.green}, blue = {self.blue}"
