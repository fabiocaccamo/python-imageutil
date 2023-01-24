from typing import List

from imageutil.core import get_color
from imageutil.types import Color


def get_average_color(
    colors: List[Color],
) -> Color:
    """
    Calculates the average color.

    :param colors: The colors
    :type colors: list of Colors

    :returns: The average color.
    :rtype: Color
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


def get_color_brightness(
    color: Color,
) -> int:
    """
    Gets the color brightness.

    :param color: The color
    :type color: Color

    :returns: The color brightness (0-255).
    :rtype: int
    """
    # https://www.w3.org/TR/AERT/#color-contrast
    # ((Red value X 299) + (Green value X 587) + (Blue value X 114)) / 1000 > 186
    # https://stackoverflow.com/questions/3942878/how-to-decide-font-color-in-white-or-black-depending-on-background-color
    r_lum = color[0] * 299
    g_lum = color[1] * 587
    b_lum = color[2] * 114
    return int(round((r_lum + g_lum + b_lum) / 1000))


def get_color_brightness_normalized(
    color: Color,
) -> float:
    """
    Gets the color brightness (normalized).

    :param color: The color
    :type color: Color

    :returns: The color brightness normalized (0.0-1.0).
    :rtype: float
    """
    brightness = get_color_brightness(color)
    brightness_norm = brightness / 255
    return brightness_norm


def get_colors_distance(
    color1: Color,
    color2: Color,
) -> int:
    """
    Calculates the distance between two colors.

    :param color1: The color 1
    :type color1: Color
    :param color2: The color 2
    :type color2: Color

    :returns: The colors distance (0-195075).
    :rtype: int
    """
    color1 = get_color(color1)
    color2 = get_color(color2)
    r1, g1, b1, a1 = color1
    r2, g2, b2, a2 = color2
    return (
        max((r1 - r2) ** 2, (r1 - r2 - a1 + a2) ** 2)
        + max((g1 - g2) ** 2, (g1 - g2 - a1 + a2) ** 2)
        + max((b1 - b2) ** 2, (b1 - b2 - a1 + a2) ** 2)
    )


def get_colors_distance_normalized(
    color1: Color,
    color2: Color,
) -> float:
    """
    Calculates the distance between two colors (normalized).

    :param color1: The color 1
    :type color1: Color
    :param color2: The color 2
    :type color2: Color

    :returns: The colors distance normalized (0.0-1.0).
    :rtype: float
    """
    # max_colors_distance = get_colors_distance((0, 0, 0, 255), (255, 255, 255, 255))
    max_colors_distance = 195075
    colors_distance = get_colors_distance(color1, color2)
    colors_distance_norm = colors_distance / max_colors_distance
    return colors_distance_norm
