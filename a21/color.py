from collections import namedtuple


class Color(namedtuple("Color", "red green blue", defaults=[0, 0, 0])):
    def __repr__(self):
        return f"Color: red = {self.red}, green = {self.green}, blue = {self.blue}"
