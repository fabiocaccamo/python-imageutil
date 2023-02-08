from __future__ import annotations

from pathlib import Path
from typing import Literal

from imageutil.pil import PILImageObject

__all__ = [
    "AnchorName",
    "AnchorIn",
    "AnchorOut",
    "RGBAColor",
    "RGBColor",
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
AnchorOut = tuple[float, float]

RGBAColor = tuple[int, int, int, int] | list[int]
RGBColor = tuple[int, int, int] | list[int]

ColorIn = RGBAColor | RGBColor
ColorOut = RGBAColor

ImagePathIn = str | Path
ImagePathOut = str

ImageIn = ImagePathIn | PILImageObject
ImageOut = PILImageObject
