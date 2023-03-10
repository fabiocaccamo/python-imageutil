from __future__ import annotations

from imageutil.args import get_color
from imageutil.types import ColorIn, ColorOut

__all__ = [
    "get_average_color",
    "get_color_brightness",
    "get_color_brightness_normalized",
    "get_colors_distance",
    "get_colors_distance_normalized",
]


def get_average_color(colors: list[ColorIn]) -> ColorOut:
    """
    Calculates the average color.

    :param colors: The colors
    :type colors: list of Colors

    :returns: The average color.
    :rtype: ColorOut
    """
    r_sum, g_sum, b_sum, a_sum = 0, 0, 0, 0
    for color in colors:
        rgba = get_color(color)
        r, g, b, a = rgba
        r_sum += r
        g_sum += g
        b_sum += b
        a_sum += a
    num_colors = len(colors)
    return (
        int(round(r_sum / num_colors)),
        int(round(g_sum / num_colors)),
        int(round(b_sum / num_colors)),
        int(round(a_sum / num_colors)),
    )


def get_color_brightness(color: ColorIn) -> int:
    """
    Gets the color brightness.

    :param color: The color
    :type color: ColorIn

    :returns: The color brightness (0-255).
    :rtype: int
    """
    # https://www.w3.org/TR/AERT/#color-contrast
    # ((Red value X 299) + (Green value X 587) + (Blue value X 114)) / 1000 > 186
    # https://stackoverflow.com/questions/3942878/how-to-decide-font-color-in-white-or-black-depending-on-background-color
    rgba = get_color(color)
    r, g, b, _ = rgba
    r_lum = r * 299
    g_lum = g * 587
    b_lum = b * 114
    return int(round((r_lum + g_lum + b_lum) / 1000))


def get_color_brightness_normalized(color: ColorIn) -> float:
    """
    Gets the color brightness (normalized).

    :param color: The color
    :type color: ColorIn

    :returns: The color brightness normalized (0.0-1.0).
    :rtype: float
    """
    brightness = get_color_brightness(color)
    brightness_norm = brightness / 255
    return brightness_norm


def get_colors_distance(color1: ColorIn, color2: ColorIn) -> int:
    """
    Calculates the distance between two colors.

    :param color1: The color 1
    :type color1: ColorIn
    :param color2: The color 2
    :type color2: ColorIn

    :returns: The colors distance (0-195075).
    :rtype: int
    """
    rgba1 = get_color(color1)
    rgba2 = get_color(color2)
    r1, g1, b1, a1 = rgba1
    r2, g2, b2, a2 = rgba2
    return (
        max((r1 - r2) ** 2, (r1 - r2 - a1 + a2) ** 2)
        + max((g1 - g2) ** 2, (g1 - g2 - a1 + a2) ** 2)  # noqa: W503
        + max((b1 - b2) ** 2, (b1 - b2 - a1 + a2) ** 2)  # noqa: W503
    )


def get_colors_distance_normalized(color1: ColorIn, color2: ColorIn) -> float:
    """
    Calculates the distance between two colors (normalized).

    :param color1: The color 1
    :type color1: ColorIn
    :param color2: The color 2
    :type color2: ColorIn

    :returns: The colors distance normalized (0.0-1.0).
    :rtype: float
    """
    # max_colors_distance = get_colors_distance((0, 0, 0, 255), (255, 255, 255, 255))
    max_colors_distance = 195075
    colors_distance = get_colors_distance(color1, color2)
    colors_distance_norm = colors_distance / max_colors_distance
    return colors_distance_norm
