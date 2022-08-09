from abc import ABC, abstractmethod
from typing import Tuple
from a21.color import Color
from a21.point import Point
from a21.html_doct import HtmlDoc
from a22.shape_dataclass import ShapeData


class Shape(ABC):
    def __init__(self, color: Color, position: Point, opacity: float) -> None:
        self._color = color
        self._position = position
        self._opacity = opacity

    def write_shape_line(self, hd: HtmlDoc) -> None:
        shape_string: str = self.line_header() + self.position_string() + self.characteristic_string() + \
                            self.color_string() + self.line_tail()
        hd.write_html_line(2, shape_string)

    @abstractmethod
    def line_header(self) -> str:
        ...

    @abstractmethod
    def line_tail(self) -> str:
        ...

    @abstractmethod
    def characteristic_string(self) -> str:
        ...

    def color_string(self) -> str:
        return f' fill="rgb({self._color.red}, {self._color.green}, {self._color.blue})" fill-opacity="{self._opacity}">'

    @abstractmethod
    def position_string(self) -> str:
        ...

    @classmethod
    @abstractmethod
    def construct_from_shape_data(cls, shape_data: ShapeData):
        ...

    @staticmethod
    def get_color_point(shape_data: ShapeData) -> Tuple[Color, Point]:
        """
        Static method to get the color and the point object out of a ShapeData dataclass
        :param shape_data: the data of the shape
        :return:
        """
        color: Color = Color(shape_data.red, shape_data.green, shape_data.blue)
        position: Point = Point(shape_data.x, shape_data.y)
        return color, position
