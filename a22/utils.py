from dataclasses import fields
from typing import Sequence

import numpy as np

from a22.art_config import ArtConfig
from a22.random_util import RandomUtil

from a22.shape_dataclass import ShapeData


def attribute_compatibility_shape_art_config() -> dict:
    """
    Function to return the matching dict of attributes between the ShapeData object and the ArtConfig object
    :return:
    """
    return {attribute.name: {"name": attribute.name + "_range",
                             "data_type": attribute.type} for attribute in fields(ShapeData)}


def generate_shape_data(art_config: ArtConfig) -> ShapeData:
    """
    Function to compute a ShapeData dataclass
    :param art_config: the aart_config to use, defining the ranges of random pick
    :return: the ShapeData object
    """
    attribute_dict: dict = attribute_compatibility_shape_art_config()
    random_dict = {k: RandomUtil.gen_value_in_range(*art_config.__getattribute__(v["name"]), v["data_type"]) for k, v in
                   attribute_dict.items()}
    return ShapeData(**random_dict)


def create_array(list_shapes: list[ShapeData]) -> np.ndarray:
    """
    Function to return the canvas array containing the shape data, and adding a header.
    :param list_shapes: the list of shapes to put in the array
    :return: the array with all shapes data, converted to string
    """
    header_dict: dict = {
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
    canvas: np.ndarray = np.empty((len(list_shapes) + 1, len(header_dict) + 1), dtype="U100")
    canvas[0, :] = ["CNT"] + list(header_dict.keys())
    for index, value in enumerate(list_shapes):
        canvas[index+1, :] = [index] + [value.__getattribute__(header_dict[canvas[0, k+1]]) for k in range(len(header_dict.keys()))]
    return canvas.astype(str)


def right_justify_string_sequence(string_list: Sequence[str]) -> list[str]:
    """
    Function to right justify a list of string. It need to find the longest string, and then right justify other strings according to this string.
    :param string_list: the string list
    :return:
    """
    max_string: int = len(max(string_list, key= lambda item: len(item)))
    new_list: list[str] = [f"{string:>{max_string}}  " for string in string_list]
    return new_list
