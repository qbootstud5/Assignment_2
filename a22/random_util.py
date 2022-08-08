import random
from typing import Union


class RandomUtil:
    @classmethod
    def gen_int_in_range(cls, min_value: Union[int, float], max_value: Union[int, float]) -> int:
        if min_value.is_integer():
            raise TypeError(f"The min_value should be an integer, not {min_value}")
        if max_value.is_integer():
            raise TypeError(f"The max_value should be an integer, not {max_value}")
        return random.randint(min_value, max_value)

    @classmethod
    def gen_float_in_range(cls, min_value: Union[int, float], max_value: Union[int, float]) -> float:
        try:
            float_min = float(min_value)
        except ValueError:
            raise ValueError("The given min_value cannot be converted to float")

        try:
            float_max = float(max_value)
        except ValueError:
            raise ValueError("The given max_value cannot be converted to float")

        return random.uniform(float_min, float_max)


