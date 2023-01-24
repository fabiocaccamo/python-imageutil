import unittest

from imageutil.core import get_alpha, get_anchor, get_color
from imageutil.exceptions import InvalidAnchorError, InvalidColorError


class CoreTestCase(unittest.TestCase):
    """
    This class describes metadata test case.
    """

    def test_get_alpha(self):
        self.assertEqual(get_alpha(-1.0), 0)
        self.assertEqual(get_alpha(0.0), 0)
        self.assertEqual(get_alpha(0.5), 128)
        self.assertEqual(get_alpha(1.0), 255)
        self.assertEqual(get_alpha(2.0), 255)

    def test_get_anchor(self):
        self.assertEqual(get_anchor("top-left"), (0.0, 0.0))
        self.assertEqual(get_anchor("top"), (0.5, 0.0))
        self.assertEqual(get_anchor("top-right"), (1.0, 0.0))
        self.assertEqual(get_anchor("left"), (0.0, 0.5))
        self.assertEqual(get_anchor("center"), (0.5, 0.5))
        self.assertEqual(get_anchor("right"), (1.0, 0.5))
        self.assertEqual(get_anchor("bottom-left"), (0.0, 1.0))
        self.assertEqual(get_anchor("bottom"), (0.5, 1.0))
        self.assertEqual(get_anchor("bottom-right"), (1.0, 1.0))

    def test_get_anchor_with_anchor_name_variant(self):
        self.assertEqual(get_anchor(" Top Left "), (0.0, 0.0))
        self.assertEqual(get_anchor(" Top "), (0.5, 0.0))
        self.assertEqual(get_anchor(" Top_Right "), (1.0, 0.0))
        self.assertEqual(get_anchor(" Left "), (0.0, 0.5))
        self.assertEqual(get_anchor(" Center "), (0.5, 0.5))
        self.assertEqual(get_anchor(" Right "), (1.0, 0.5))
        self.assertEqual(get_anchor(" Bottom Left "), (0.0, 1.0))
        self.assertEqual(get_anchor(" Bottom "), (0.5, 1.0))
        self.assertEqual(get_anchor(" Bottom_Right "), (1.0, 1.0))

    def test_get_anchor_with_invalid_anchor_name(self):
        with self.assertRaises(InvalidAnchorError):
            get_anchor("top-left-right")

    def test_get_color(self):
        self.assertEqual(get_color(), (255, 255, 255, 255))

    def test_get_color_with_rgba(self):
        self.assertEqual(get_color((255, 255, 255, 128)), (255, 255, 255, 128))

    def test_get_color_with_rgb(self):
        self.assertEqual(get_color((255, 255, 255)), (255, 255, 255, 255))

    def test_get_color_with_rgba_and_opacity(self):
        self.assertEqual(get_color((255, 255, 255, 255), 0.5), (255, 255, 255, 128))

    def test_get_color_with_rgb_and_opacity(self):
        self.assertEqual(get_color((255, 255, 255), 0.5), (255, 255, 255, 128))

    def test_get_color_with_rgba_list(self):
        self.assertEqual(get_color([255, 255, 255, 128]), (255, 255, 255, 128))

    def test_get_color_with_invalid_color(self):
        with self.assertRaises(InvalidColorError):
            get_color((255, 255))
        with self.assertRaises(InvalidColorError):
            get_color((255, 255, 255, 255, 255))
