from pathlib import Path
from typing import Optional

import fsutil

from imageutil.exceptions import (
    InvalidAnchorError,
    InvalidColorError,
    InvalidImageError,
)
from imageutil.pil import PILImage, PILImageObject
from imageutil.types import AnchorIn, AnchorOut, ColorIn, ColorOut, ImageIn, ImageOut

__all__ = [
    "get_alpha",
    "get_anchor",
    "get_color",
    "get_image",
]


def get_alpha(
    opacity: float,
) -> int:
    """
    Gets the alpha (0-255 int value) mapping
    the opacity input (0.0-1.0 float value).

    :param opacity: The opacity
    :type opacity: float

    :returns: The alpha value.
    :rtype: int
    """
    # interpolate value
    alpha = int(round(255 * opacity))
    # constain value
    alpha = min(max(0, alpha), 255)
    return alpha


def get_anchor(
    name: AnchorIn,
) -> AnchorOut:
    """
    Gets the anchor converting anchor position name string
    to a tuple (x, y) where each value is a float between 0.0 and 1.0.

    :param name: The anchor name
    :type name: AnchorIn

    :returns: The anchor position.
    :rtype: AnchorOut

    :raises InvalidAnchorError: If name is not a valid anchor name.
    """
    name_value = name.strip().lower()
    name_value = name_value.replace(" ", "-").replace("_", "-").replace("--", "-")
    name_options = [
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
    if name_value not in name_options:
        raise InvalidAnchorError(name_value)

    if "left" in name_value:
        left = 0.0
    elif "right" in name_value:
        left = 1.0
    else:
        left = 0.5
    if "top" in name_value:
        top = 0.0
    elif "bottom" in name_value:
        top = 1.0
    else:
        top = 0.5
    return (left, top)


def get_color(
    color: Optional[ColorIn] = None,
    opacity: Optional[float] = None,
) -> ColorOut:
    """
    Gets the color.

    :param color: The color
    :type color: ColorIn or None
    :param opacity: The opacity value (0.0-1.0)
    :type opacity: float

    :returns: The color.
    :rtype: ColorOut

    :raises InvalidColorError: If color is not a valid RGBA / RGB color.
    """
    if color is None:
        color = (255, 255, 255, 255)

    # TODO: add hex/hexa color format support

    if len(color) not in (3, 4):
        raise InvalidColorError(color)

    color = list(color)
    if len(color) == 3:
        color.append(255)

    # override color alpha using the opacity value
    if opacity is not None:
        alpha = get_alpha(opacity)
        color[3] = alpha

    # constain value
    r, g, b, a = color
    r = min(max(0, r), 255)
    g = min(max(0, g), 255)
    b = min(max(0, b), 255)
    a = min(max(0, a), 255)

    # convert color back to tuple and return it
    color = (r, g, b, a)
    return color


def get_image(
    src: ImageIn,
    copy: bool = True,
) -> ImageOut:
    """
    Gets the image.

    :param src: The source for an image object.
    :type src: ImageIn
    :param copy: The copy flag, if True copies the src PIL image.
    :type copy: bool

    :returns: The PIL image object.
    :rtype: ImageOut

    :raises InvalidImageError: If src is not a valid filepath / URL / PIL image.
    """
    if isinstance(src, (str, Path)):
        image_src = str(src)
        if image_src.startswith("https://") or image_src.startswith("http://"):
            image_filepath = fsutil.download_file(image_src)
        else:
            image_filepath = image_src
        image = PILImage.open(image_filepath)
    elif isinstance(src, PILImageObject):
        image = src.copy() if copy else src
    else:
        raise InvalidImageError(src)
    return image
