from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class ShapeData:
    """
    Shape dataclass to store values defining a shape
    """
    # For position
    x: int
    y: int
    # SHA
    sha: int
    # For colors
    red: int
    green: int
    blue: int

    # For circle radius
    circ_radius: int

    # For ellipse radiuses
    ellipse_rx: int
    ellipse_ry: int

    # Rectangle_width
    rect_width: int
    rect_height: int

    # Opacity
    opacity: float
