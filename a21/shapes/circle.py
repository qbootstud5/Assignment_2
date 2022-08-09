from a21.shapes.shape import Shape
from a22.shape_dataclass import ShapeData
from a21.color import Color
from a21.point import Point


class Circle(Shape):
    """
    Class for the circle
    """
    def __init__(self, color: Color, position: Point, opacity: float, rad: int) -> None:
        """
        Constructor for the circle
        :param color:
        :param position:
        :param opacity:
        :param rad: radius of the circle
        """
        super().__init__(color, position, opacity)
        self.__rad = rad

    def line_header(self) -> str:
        return "<circle"

    def line_tail(self) -> str:
        return "</circle>"

    def characteristic_string(self) -> str:
        return f'r="{self.__rad}"'

    def position_string(self) -> str:
        return f' cx="{self._position.x}" cy="{self._position.y}" '

    @classmethod
    def construct_from_shape_data(cls, shape_data: ShapeData):
        """
        Alternative constructor to construct from a data object
        :param shape_data: the data object containing the information of the circle
        :return:
        """
        color, position = cls.get_color_point(shape_data)
        return cls(color, position, shape_data.opacity, shape_data.circ_radius)
