from a21.shapes.shape import Shape
from a21.color import Color
from a21.point import Point


class Circle(Shape):
    def __init__(self, color: Color, position: Point, opacity: float, rad: int) -> None:
        super().__init__(color, position, opacity)
        self.__rad = rad

    def line_header(self) -> str:
        return "<circle"

    def line_tail(self) -> str:
        return "</circle>"

    def characteristic_string(self) -> str:
        return f'r="{self.__rad}"'
