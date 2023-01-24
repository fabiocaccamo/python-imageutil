import unittest

from imageutil.colors import (
    get_average_color,
    get_color_brightness,
    get_color_brightness_normalized,
    get_colors_distance,
    get_colors_distance_normalized,
)


class ColorsTestCase(unittest.TestCase):
    """
    This class describes metadata test case.
    """

    def test_get_average_color(self):
        self.assertEqual(
            get_average_color(
                [
                    (255, 255, 255),
                    (0, 0, 0),
                ]
            ),
            (128, 128, 128, 255),
        )

    def test_get_color_brightness(self):
        self.assertEqual(get_color_brightness((255, 255, 255)), 255)
        self.assertEqual(get_color_brightness((255, 0, 0)), 76)
        self.assertEqual(get_color_brightness((0, 255, 0)), 150)
        self.assertEqual(get_color_brightness((0, 0, 255)), 29)
        self.assertEqual(get_color_brightness((0, 0, 0)), 0)

    def test_get_color_brightness_normalized(self):
        def f(color):
            return round(get_color_brightness_normalized(color), 3)

        self.assertEqual(f((255, 255, 255)), 1.0)
        self.assertEqual(f((255, 0, 0)), 0.298)
        self.assertEqual(f((0, 255, 0)), 0.588)
        self.assertEqual(f((0, 0, 255)), 0.114)
        self.assertEqual(f((0, 0, 0)), 0.0)

    def test_get_colors_distance(self):
        distance = get_colors_distance((255, 255, 255), (0, 0, 0))
        self.assertEqual(distance, 195075)
        distance = get_colors_distance((128, 128, 128), (0, 0, 0))
        self.assertEqual(distance, 49152)

    def test_get_colors_distance_normalized(self):
        def f(color1, color2):
            return round(get_colors_distance_normalized(color1, color2), 3)

        distance = f((255, 255, 255), (0, 0, 0))
        self.assertEqual(distance, 1.0)
        distance = f((128, 128, 128), (0, 0, 0))
        self.assertEqual(distance, 0.252)
