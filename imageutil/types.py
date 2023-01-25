from typing import List, Literal, Tuple, Union

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

AnchorIn = AnchorName
AnchorOut = Tuple[float, float]

RGBAColor = Union[Tuple[int, int, int, int], List[int]]
RGBColor = Union[Tuple[int, int, int], List[int]]

ColorIn = Union[RGBAColor, RGBColor]
ColorOut = RGBAColor
