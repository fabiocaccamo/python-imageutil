import unittest

from imageutil.metadata import (
    __author__,
    __copyright__,
    __description__,
    __email__,
    __license__,
    __title__,
    __version__,
)


class MetadataTestCase(unittest.TestCase):
    """
    This class describes metadata test case.
    """

    def test_variables(self):
        self.assertTrue(bool(__author__))
        self.assertTrue(bool(__copyright__))
        self.assertTrue(bool(__description__))
        self.assertTrue(bool(__email__))
        self.assertTrue(bool(__license__))
        self.assertTrue(bool(__title__))
        self.assertTrue(bool(__version__))
