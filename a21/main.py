#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday July 29
@author: Jon Oillarburu

This file solves the Assignment 2.1
"""

from color import Color
from html_doct import HtmlDoc
from point import Point
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.ellipse import Ellipse
from svg_canvas import SvgCanvas

from pathlib import Path

dir_path = Path(__file__).parent



def test_shape() -> list:
    """
    Test function to run the main script
    :return:
    """
    color = Color(2, 3, 4)
    point = Point(10, 15)
    opacity = 0.5
    circle = Circle(color, point, opacity, 10)

    ellipse = Ellipse(color, point, opacity, 13, 15)

    rect = Rectangle(color, point, opacity, 34, 36)

    return [circle, ellipse, rect]


def main() -> None:
    """
    Main script running function
    :return:
    """
    hd: HtmlDoc = HtmlDoc(dir_path / "part1.html", "MyPart1")
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
