from imageutil.types import ImageIn

__all__ = [
    "open",
]


def open(image_src: ImageIn):
    """
    Load an image from the given source.

    :param image_src: The image source
    :type image_src: ImageIn

    :returns: The image object (should be used as context manager).
    :rtype: Image
    """
    from imageutil import Image

    return Image.open(image_src)
