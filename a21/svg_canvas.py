from typing import Union, List

from a21.html_doct import HtmlDoc
from a21.shapes.circle import Circle
from a21.shapes.ellipse import Ellipse
from a21.shapes.rectangle import Rectangle


class SvgCanvas:
    def __init__(self, width: int, height: int) -> None:
        self.__width: int = width
        self.__height: int = height

    def write_svg_header(self, hd: HtmlDoc) -> None:
        hd.write_html_line(1,f'<div style="text-align:center;">')
        hd.write_html_line(1, f'<svg width="{self.__width}" height="{self.__height}">')

    @staticmethod
    def write_svg_tail(hd: HtmlDoc) -> None:
        hd.write_html_line(1, "</svg>")
        hd.write_html_line(1, "</div>")

    @staticmethod
    def gen_art(hd: HtmlDoc, shape_list: List[Union[Circle, Rectangle, Ellipse]]) -> None:
        for shape in shape_list:
            shape.write_shape_line(hd)
