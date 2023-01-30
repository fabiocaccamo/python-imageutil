import unittest

from imageutil.core import Image
from imageutil.pil import PILImageObject


class CoreTestCase(unittest.TestCase):
    """
    This class describes a core test case.
    """

    def test_image_constructor(self):
        image_src = "./tests/images/python-logo.png"
        image = Image(image_src)
        self.assertTrue(isinstance(image, Image))
        self.assertTrue(isinstance(image.pil_image, PILImageObject))
        image.close()

    def test_image_constructor_with_invalid_image(self):
        image_src = "./tests/images/python-logo-invalid.png"
        with self.assertRaises(FileNotFoundError):
            Image(image_src)

    def test_image_constructor_as_context_manager(self):
        image_src = "./tests/images/python-logo.png"
        with Image(image_src) as image:
            self.assertTrue(isinstance(image, Image))
            self.assertTrue(isinstance(image.pil_image, PILImageObject))

    def test_image_load(self):
        image_src = "./tests/images/python-logo.png"
        image = Image.load(image_src)
        self.assertTrue(isinstance(image, Image))
        self.assertTrue(isinstance(image.pil_image, PILImageObject))
        image.close()

    def test_image_load_with_invalid_image(self):
        image_src = "./tests/images/python-logo-invalid.png"
        with self.assertRaises(FileNotFoundError):
            Image.load(image_src)

    def test_image_load_as_context_manager(self):
        image_src = "./tests/images/python-logo.png"
        with Image.load(image_src) as image:
            self.assertTrue(isinstance(image, Image))
            self.assertTrue(isinstance(image.pil_image, PILImageObject))

    def test_image_get_attr_method_of_wrapped_pil_image(self):
        image_src = "./tests/images/python-logo.png"
        with Image(image_src) as image:
            image.rotate(90)
            # image.show()

    def test_image_get_attr_property_of_wrapped_pil_image(self):
        image_src = "./tests/images/python-logo.png"
        with Image(image_src) as image:
            size = image.size
            self.assertEqual(size, (1200, 1200))

    def test_image_get_attr_invalid(self):
        image_src = "./tests/images/python-logo.png"
        with Image(image_src) as image:
            with self.assertRaises(AttributeError):
                image.invalid_attribute()
