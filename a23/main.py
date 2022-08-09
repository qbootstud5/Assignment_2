#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday August 09
@author: Jon Oillarburu

This file solves the Assignment 2.3

6 Art style are available:
- all_random
- opaque
- green shades
- green circles
- red rectangles
- blue ellipses

"""
from a22.art_config import ArtConfig
from a23.configuration_class import Configuration


def all_random_config(num_shapes: int, svg_size: tuple[int, int] = (800, 800)):
    """
    All random config
    :param num_shapes: number of shapes to draw
    :param svg_size: the svg size
    :return:
    """
    art_config: ArtConfig = ArtConfig(
        x_range=(0, svg_size[0]),
        y_range=(0, svg_size[1]),
    )
    config: Configuration = Configuration(num_shapes, art_config, *svg_size)

    config.write_html("part3_all_random.html", "Mypart3_1")


def opaque_config(num_shapes: int, svg_size: tuple[int, int] = (800, 800)):
    """
    Opaque style
    :param num_shapes: number of shapes to draw
    :param svg_size: the svg size
    :return:
    """
    art_config: ArtConfig = ArtConfig(
        x_range=(0, svg_size[0]),
        y_range=(0, svg_size[1]),
        opacity_range=(0.8, 1)
    )
    config: Configuration = Configuration(num_shapes, art_config, *svg_size)

    config.write_html("part3_opacity.html", "Mypart3_1")


def green_shades(num_shapes: int, svg_size: tuple[int, int] = (800, 800)):
    """
    Green shades style
    :param num_shapes: number of shapes to draw
    :param svg_size: the svg size
    :return:
    """
    art_config: ArtConfig = ArtConfig(
        x_range=(0, svg_size[0]),
        y_range=(0, svg_size[1]),
        red_range=(0, 0),
        blue_range=(0, 0)
    )
    config: Configuration = Configuration(num_shapes, art_config, *svg_size)

    config.write_html("part3_green_shades.html", "Mypart3_1")


def configuration_green_circle(num_shapes: int, svg_size: tuple[int, int] = (800, 800)):
    """
    Green circles
    :param num_shapes: number of shapes to draw
    :param svg_size: the svg size
    :return:
    """
    art_config: ArtConfig = ArtConfig(
        x_range=(0, svg_size[0]),
        y_range=(0, svg_size[1]),
        sha_range=(0, 0),
        red_range=(0, 0),
        blue_range=(0, 0),
        circ_radius_range=(100, 200)
    )
    config: Configuration = Configuration(num_shapes, art_config, *svg_size)

    config.write_html("part3_green_circles.html", "Mypart3_1")


def configuration_red_rectangle(num_shapes: int, svg_size: tuple[int, int] = (800, 800)):
    """
    Red rectangles
    :param num_shapes: number of shapes to draw
    :param svg_size: the svg size
    :return:
    """
    art_config: ArtConfig = ArtConfig(
        x_range=(0, svg_size[0]),
        y_range=(0, svg_size[1]),
        sha_range=(1, 1),
        green_range=(0, 0),
        blue_range=(0, 0),
        rect_width_range=(100, 200),
        rect_height_range=(100, 200)
    )
    config: Configuration = Configuration(num_shapes, art_config, *svg_size)

    config.write_html("part3_red_rectangles.html", "Mypart3_1")


def configuration_blue_ellipse(num_shapes: int, svg_size: tuple[int, int] = (800, 800)):
    """
    Blue ellipses
    :param num_shapes: number of shapes to draw
    :param svg_size: the svg size
    :return:
    """
    art_config: ArtConfig = ArtConfig(
        x_range=(0, svg_size[0]),
        y_range=(0, svg_size[1]),
        sha_range=(2, 2),
        red_range=(0, 0),
        green_range=(0, 0),
        ellipse_rx_range=(100, 200),
        ellipse_ry_range=(100, 200)
    )
    config: Configuration = Configuration(num_shapes, art_config, *svg_size)

    config.write_html("part3_blue_ellipses.html", "Mypart3_1")


def main():
    all_random_config(1000)
    opaque_config(300)
    green_shades(300)


if __name__ == "__main__":
    main()
