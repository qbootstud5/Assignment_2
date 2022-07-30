#!/usr/bin/env python
"""Assignment 2 Part 1 running script"""

from a21.color import Color
from a21.html_doct import HtmlDoc
from a21.point import Point
from a21.shapes.circle import Circle
from a21.shapes.rectangle import Rectangle
from a21.shapes.ellipse import Ellipse
from a21.svg_canvas import SvgCanvas

def test_shape():
    color = Color(2, 3, 4)
    point = Point(10, 15)
    opacity = 0.5
    circle = Circle(color, point, opacity, 10)

    ellipse = Ellipse(color, point, opacity, 13,15)

    rect = Rectangle(color,point, opacity, 34,36)

    return [circle, ellipse, rect]


def main() -> None:
    hd: HtmlDoc = HtmlDoc("part1_test_3.html", "MyPart1")
    hd.open_html_file()
    hd.write_html_head()
    svg_canvas: SvgCanvas = SvgCanvas(width=30, height=30)
    svg_canvas.write_svg_header(hd)
    list_shape = test_shape()
    svg_canvas.gen_art(hd, list_shape)
    svg_canvas.write_svg_tail(hd)
    hd.write_html_tail()
    hd.close_html_file()


if __name__ == "__main__":
    main()
