from a21.shapes.shape import Shape
from a21.color import Color
from a21.point import Point
from a22.shape_dataclass import ShapeData


class Rectangle(Shape):
    """
    Class for the rectangle shape
    """
    def __init__(self, color: Color, position: Point, opacity: float, width: int, height: int):
        """
        Constructor for the rectangle
        :param color:
        :param position:
        :param opacity:
        :param width: width of the rectangle
        :param height: height of the rectangle
        """
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

    @classmethod
    def construct_from_shape_data(cls, shape_data: ShapeData):
        """
        Alternative constructor to construct from a data object
        :param shape_data: the data object containing the information of the rectangle
        :return:
        """
        color, position = cls.get_color_point(shape_data)
        return cls(color, position, shape_data.opacity, shape_data.rect_width, shape_data.rect_height)
