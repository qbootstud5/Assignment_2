from a21.shapes.shape import Shape
from a21.color import Color
from a21.point import Point
from a22.shape_dataclass import ShapeData


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

    @classmethod
    def construct_from_shape_data(cls, shape_data: ShapeData):
        """
        Alternative constructor to construct from a data object
        :param shape_data: the data object containing the information of the ellipse
        :return:
        """
        color, position = cls.get_color_point(shape_data)
        return cls(color, position, shape_data.opacity, shape_data.ellipse_rx, shape_data.ellipse_ry)
