from typing import Union, List

from html_doct import HtmlDoc
from shapes.circle import Circle
from shapes.ellipse import Ellipse
from shapes.rectangle import Rectangle


class SvgCanvas:
    def __init__(self, width: int, height: int) -> None:
        self.__width: int = width
        self.__height: int = height

    def write_svg_header(self, hd: HtmlDoc) -> None:
        hd.write_html_line(1, f'<svg width="{self.__width}" height="{self.__height}">')

    def write_svg_tail(self, hd: HtmlDoc) -> None:
        hd.write_html_line(1, "</svg>")

    def gen_art(self, hd: HtmlDoc, shape_list: List[Union[Circle, Rectangle, Ellipse]]) -> None:
        for shape in shape_list:
            shape.write_shape_line(hd)
