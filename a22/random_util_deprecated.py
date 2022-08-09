import random
from typing import Tuple
from a22.art_config import ArtConfig


class RandomUtil:
    # Default ranges
    x_range: Tuple[int, int]
    y_range: Tuple[int, int]
    # For colors
    red_range: Tuple[int, int]
    green_range: Tuple[int, int]
    blue_range: Tuple[int, int]

    # For circle radius
    circ_radius_range: Tuple[int, int]

    # For ellipse radiuses
    ellipse_rx_range: Tuple[int, int]
    ellipse_ry_range: Tuple[int, int]

    # Rectangle_width
    rect_width_range: Tuple[int, int]
    rect_height_range: Tuple[int, int]

    # Opacity
    opacity_range: Tuple[float, float]

    def __init__(self, art_config: ArtConfig) -> None:
        self.x_range = art_config.x_range
        self.y_range = art_config.y_range
        self.red_range = art_config.red_range
        self.green_range = art_config.green_range
        self.blue_range = art_config.blue_range
        self.circ_radius_range = art_config.circ_radius_range
        self.ellipse_rx_range = art_config.ellipse_rx_range
        self.ellipse_ry_range = art_config.ellipse_ry_range
        self.rect_width_range = art_config.rect_width_range
        self.rect_height_range = art_config.rect_height_range
        self.opacity_range = art_config.opacity_range

    @classmethod
    def gen_int_in_range(cls, variable_name: str) -> int:
        if variable_name not in cls.int_correspondency_table().keys():
            raise ValueError("The chosen feature is not implemented for int generation")
        return random.randint(*cls.int_correspondency_table()[variable_name])

    @classmethod
    def gen_float_in_range(cls, variable_name: str) -> float:
        if variable_name not in cls.float_correspondency_table().keys():
            raise ValueError("The chosen feature is not implemented for float generation")
        return random.uniform(*cls.float_correspondency_table()[variable_name])

    @classmethod
    def int_correspondency_table(cls) -> dict:
        correspondency_dict = {
            "x": cls.x_range,
            "y": cls.y_range,
            "red": cls.red_range,
            "green": cls.green_range,
            "blue": cls.blue_range,
            "circ_radius": cls.circ_radius_range,
            "ellipse_rx": cls.ellipse_rx_range,
            "ellipse_ry": cls.ellipse_ry_range,
            "rect_width": cls.rect_width_range,
            "rect_height": cls.rect_height_range
        }
        return correspondency_dict

    @classmethod
    def float_correspondency_table(cls) -> dict:
        correspondency_dict = {
            "opacity": cls.opacity_range
        }
        return correspondency_dict
