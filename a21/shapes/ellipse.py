from a21.shapes.shape import Shape
from a21.color import Color
from a21.point import Point


class Ellipse(Shape):
    def __init__(self, color: Color, position: Point, opacity: float, rx: int, ry: int):
        super().__init__(color, position, opacity)
        self.__rx = rx
        self.__ry = ry

    def line_header(self) -> str:
        return "<ellipse"

    def line_tail(self) -> str:
        return "</ellipse>"

    def characteristic_string(self) -> str:
        return f'rx="{self.__rx}" ry="{self.__ry}"'

    def position_string(self) -> str:
        return f' cx="{self._position.x}" cy="{self._position.y}" '
