from typing import Tuple


class ArtConfig:
    # Default ranges
    # For colors
    red_default_range: Tuple[int, int] = (0, 255)
    green_default_range: Tuple[int, int] = (0, 255)
    blue_default_range: Tuple[int, int] = (0, 255)

    # For circle radius
    circ_radius_default_range: Tuple[int, int] = (0, 100)

    # For ellipse radiuses
    ellipse_rx_default_range: Tuple[int, int] = (10, 30)
    ellipse_ry_default_range: Tuple[int, int] = (10, 30)

    # Rectangle_width
    rect_width_default_range: Tuple[int, int] = (10, 100)
    rect_height_default_range: Tuple[int, int] = (10, 100)

    # Opacity
    opacity_default_range: Tuple[float, float] = (0.0, 1.0)

    def __init__(self,
                 red_range: Tuple[int, int] = red_default_range,
                 green_range: Tuple[int, int] = green_default_range,
                 blue_range: Tuple[int, int] = blue_default_range,
                 circ_radius_range: Tuple[int, int] = circ_radius_default_range,
                 ellipse_rx_range: Tuple[int, int] = ellipse_rx_default_range,
                 ellipse_ry_range: Tuple[int, int] = ellipse_ry_default_range,
                 rect_width_range: Tuple[int, int] = rect_width_default_range,
                 rect_height_range: Tuple[int, int] = rect_height_default_range,
                 opacity_range: Tuple[float, float] = opacity_default_range
                 ):
        self.red_range = red_range
        self.green_range = green_range
        self.blue_range = blue_range
        self.circ_radius_range = circ_radius_range
        self.ellipse_rx_range = ellipse_rx_range
        self.ellipse_ry_range = ellipse_ry_range
        self.rect_width_range = rect_width_range
        self.rect_height_range = rect_height_range
        self.opacity_range = opacity_range
