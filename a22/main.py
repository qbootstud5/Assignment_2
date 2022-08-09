from a22.utils import generate_shape_data, create_array, right_justify_string_sequence
from shape_dataclass import ShapeData
import numpy as np
from art_config import ArtConfig


def main(number_shapes: int = 10):
    basic_art_config: ArtConfig = ArtConfig(x_range=(0, 1000), y_range=(0, 1000))
    list_shapes: list[ShapeData] = [generate_shape_data(basic_art_config) for k in range(number_shapes)]

    canvas: np.ndarray = create_array(list_shapes)

    for column_name in range(canvas.shape[1]):
        canvas[:,column_name] = right_justify_string_sequence(canvas[:, column_name])

    final_string: str = "\n".join(["".join(row) for row in canvas])

    print(final_string)


if __name__ == "__main__":
    main()
