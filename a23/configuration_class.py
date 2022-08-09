from typing import Union
from a21.shapes.circle import Circle
from a21.shapes.rectangle import Rectangle
from a21.shapes.ellipse import Ellipse
from a21.html_doct import HtmlDoc
from a21.svg_canvas import SvgCanvas
from a22.art_config import ArtConfig
from a22.shape_dataclass import ShapeData
from a22.utils import generate_shape_data


class Configuration:

    def __init__(self, number_shape: int, art_config: ArtConfig, svg_width: int, svg_height: int) -> None:
        """
        Constructor method. Automatically computes the ShapeData dataclasses
        :param number_shape: the number of shape
        :param art_config: the defined art configuration
        :param svg_width: the width of the svg canvas
        :param svg_height: the height of the svg canvas
        """
        self.art_config: ArtConfig = art_config
        self.svg_width: int = svg_width
        self.svg_height: int = svg_height
        self.number_shape: int = number_shape
        self.list_shape_data: list[ShapeData] = self.create_list_shape()

    def create_list_shape(self) -> list[ShapeData]:
        """
        Function to create list of shapes
        :return:
        """
        return [generate_shape_data(self.art_config) for k in range(self.number_shape)]

    @staticmethod
    def correspondency_sha_dict() -> dict:
        """
        The correspondency dictionary between the sha in the ShapeData class and the actual class
        :return:
        """
        return {
            0: Circle,
            1: Rectangle,
            2: Ellipse
        }

    def convert_into_shape_class(self, shape_data: ShapeData) -> Union[Circle, Rectangle, Ellipse]:
        """
        The method to construct the shapes from the ShapeData dataclasses
        :param shape_data:
        :return:
        """
        return self.correspondency_sha_dict()[shape_data.sha].construct_from_shape_data(shape_data)

    def compute_title_string(self, title: str):
        return title.center(self.svg_width, "-")

    def write_html(self, file_path: str, title: str) -> None:
        """
        The method to write the html file
        :param file_path:
        :param title:
        :return:
        """
        hd: HtmlDoc = HtmlDoc(file_path, title)
        # Open file
        hd.open_html_file()
        # Write head
        hd.write_html_head()
        # Write the svg title:
        image_title = f'{self.svg_width}x{self.svg_width}; {self.number_shape} shapes'
        hd.write_html_line(1, f"<h1>{image_title}</h1>")
        # Write the svg lines
        svg_canvas: SvgCanvas = SvgCanvas(width=self.svg_width, height=self.svg_height)
        svg_canvas.write_svg_header(hd)
        list_shape = [self.convert_into_shape_class(shape) for shape in self.list_shape_data]
        svg_canvas.gen_art(hd, list_shape)
        svg_canvas.write_svg_tail(hd)
        # Write the tail
        hd.write_html_tail()
        # Close file
        hd.close_html_file()
