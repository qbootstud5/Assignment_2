from dataclasses import fields
from shape_dataclass import ShapeData
import numpy as np
from random_util import RandomUtil
from art_config import ArtConfig
from typing import Sequence


def attribute_compatibility_shape_art_config() -> dict:
    return {attribute.name: {"name": attribute.name + "_range",
                             "data_type": attribute.type} for attribute in fields(ShapeData)}


def generate_shape_data(art_config: ArtConfig) -> ShapeData:
    attribute_dict: dict = attribute_compatibility_shape_art_config()
    random_dict = {k: RandomUtil.gen_value_in_range(*art_config.__getattribute__(v["name"]), v["data_type"]) for k, v in
                   attribute_dict.items()}
    return ShapeData(**random_dict)


def create_array(list_shapes: list[ShapeData]) -> np.ndarray:
    header_dict = {
        "SHA": "sha",
        "X": "x",
        "Y": "y",
        "RAD": "circ_radius",
        "RX": "ellipse_rx",
        "RY": "ellipse_ry",
        "W": "rect_width",
        "H": "rect_height",
        "R": "red",
        "G": "green",
        "B": "blue",
        "OP": "opacity"
    }
    canvas = np.empty((len(list_shapes) + 1, len(header_dict) + 1), dtype="U100")
    canvas[0, :] = ["CNT"] + list(header_dict.keys())
    for index, value in enumerate(list_shapes):
        canvas[index+1, :] = [index] + [value.__getattribute__(header_dict[canvas[0, k+1]]) for k in range(len(header_dict.keys()))]
    return canvas.astype(str)


def right_justify_string_sequence(string_list: Sequence) -> list[str]:
    max_string = len(max(string_list, key= lambda item: len(item)))
    new_list = [f"{string:>{max_string}}  " for string in string_list]
    return new_list


def main(number_shapes: int = 10):
    basic_art_config: ArtConfig = ArtConfig(x_range=(0, 1000), y_range=(0, 1000))
    list_shapes: list[ShapeData] = [generate_shape_data(basic_art_config) for k in range(number_shapes)]

    canvas: np.ndarray = create_array(list_shapes)

    for column_name in range(canvas.shape[1]):
        canvas[:,column_name] = right_justify_string_sequence(canvas[:,column_name])

    final_string: str = "\n".join(["".join(row) for row in canvas])

    print(final_string)


if __name__ == "__main__":
    main()
