from typing import Tuple
from dataclasses import dataclass



@dataclass(frozen=True)
class ArtConfig:
    # Default ranges
    x_range: Tuple[int,int]
    y_range: Tuple[int,int]
    # For colors
    red_range: Tuple[int, int] = (0, 255)
    green_range: Tuple[int, int] = (0, 255)
    blue_range: Tuple[int, int] = (0, 255)

    # For circle radius
    circ_radius_range: Tuple[int, int] = (0, 100)

    # For ellipse radiuses
    ellipse_rx_range: Tuple[int, int] = (10, 30)
    ellipse_ry_range: Tuple[int, int] = (10, 30)

    # Rectangle_width
    rect_width_range: Tuple[int, int] = (10, 100)
    rect_height_range: Tuple[int, int] = (10, 100)

    # Opacity
    opacity_range: Tuple[float, float] = (0.0, 1.0)
