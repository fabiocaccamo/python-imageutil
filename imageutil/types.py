from typing import Literal, Union

Anchor = tuple[float, float]
AnchorName = Literal[
    "bottom",
    "bottom-left",
    "bottom-right",
    "center",
    "left",
    "right",
    "top",
    "top-left",
    "top-right",
]
RGBAColor = Union[tuple[int, int, int, int], list[int]]
RGBColor = Union[tuple[int, int, int], list[int]]
Color = Union[RGBAColor, RGBColor]
