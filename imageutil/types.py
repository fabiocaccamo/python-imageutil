from typing import List, Literal, Tuple, Union

Anchor = Tuple[float, float]
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
RGBAColor = Union[Tuple[int, int, int, int], List[int]]
RGBColor = Union[Tuple[int, int, int], List[int]]
Color = Union[RGBAColor, RGBColor]
