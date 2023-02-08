from __future__ import annotations

from pathlib import Path
from typing import List, Literal, Tuple, Union

from imageutil.pil import PILImageObject

__all__ = [
    "AnchorName",
    "AnchorIn",
    "AnchorOut",
    "ColorIn",
    "ColorOut",
    "ImagePathIn",
    "ImagePathOut",
    "ImageIn",
    "ImageOut",
]

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

ColorIn = Union[float, int, Tuple[int, int, int], Tuple[int, int, int, int], List[int]]
ColorOut = Tuple[int, int, int, int]

ImagePathIn = Union[str, Path]
ImagePathOut = str

ImageIn = Union[ImagePathIn, PILImageObject]
ImageOut = PILImageObject
