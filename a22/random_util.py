import random
from typing import Union


class RandomUtil:
    """
    RandomUtil dataclass to create random shapes
    """
    @classmethod
    def gen_int_in_range(cls, min_value: Union[int, float], max_value: Union[int, float]) -> int:
        if not isinstance(min_value, int):
            if min_value.is_integer():
                raise TypeError(f"The min_value should be an integer, not {min_value}")
        if not isinstance(max_value, int):
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

        return round(random.uniform(float_min, float_max), 2)

    @classmethod
    def gen_value_in_range(cls, min_value: Union[int, float], max_value: Union[int, float], value_type:str = float):
        if value_type == float:
            return cls.gen_float_in_range(min_value, max_value)
        elif value_type == int:
            return cls.gen_int_in_range(min_value, max_value)
        else:
            raise NotImplementedError


