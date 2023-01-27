import unittest
from pathlib import Path

from imageutil.core import get_alpha, get_anchor, get_color, get_image
from imageutil.exceptions import (
    InvalidAnchorError,
    InvalidColorError,
    InvalidImageError,
)
from imageutil.pil import PILImage, PILImageObject


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

    def test_get_image_with_str_filepath(self):
        image_src = "./tests/images/python-logo.png"
        image = get_image(image_src)
        self.assertTrue(isinstance(image, PILImageObject))
        self.assertEqual(image.size, (1200, 1200))
        image.close()

    def test_get_image_with_pathlib_path(self):
        image_src = Path("./tests/images/python-logo.png")
        image = get_image(image_src)
        self.assertTrue(isinstance(image, PILImageObject))
        self.assertEqual(image.size, (1200, 1200))
        image.close()

    def test_get_image_with_url(self):
        image_src = (
            "https://raw.githubusercontent.com/fabiocaccamo"
            "/python-imageutil/main/tests/images/python-logo.png"
        )
        image = get_image(image_src)
        self.assertTrue(isinstance(image, PILImageObject))
        self.assertEqual(image.size, (1200, 1200))
        image.close()

    def test_get_image_with_pil_image_with_copy(self):
        image_src = PILImage.new("RGBA", (10, 10), (0, 0, 0, 0))
        image = get_image(image_src, copy=True)
        self.assertTrue(isinstance(image, PILImageObject))
        self.assertFalse(image_src is image)
        self.assertEqual(image_src.size, image.size)
        image.close()

    def test_get_image_with_pil_image_without_copy(self):
        image_src = PILImage.new("RGBA", (10, 10), (0, 0, 0, 0))
        image = get_image(image_src, copy=False)
        self.assertTrue(isinstance(image, PILImageObject))
        self.assertTrue(image_src is image)
        self.assertEqual(image_src.size, image.size)
        image.close()

    def test_get_image_with_invalid_source(self):
        with self.assertRaises(InvalidImageError):
            get_image(None)
