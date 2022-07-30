from a21.shapes.shape import Shape
from a21.color import Color
from a21.point import Point


class Rectangle(Shape):
    def __init__(self, color: Color, position: Point, opacity: float, width: int, height: int):
        super().__init__(color, position, opacity)
        self.__width = width
        self.__height = height

    def line_header(self) -> str:
        return "<rect"

    def line_tail(self) -> str:
        return "</rect>"

    def characteristic_string(self) -> str:
        return f'width="{self.__width}" height="{self.__height}"'

    def position_string(self) -> str:
        return f' x="{self._position.x}" y="{self._position.y}" '
