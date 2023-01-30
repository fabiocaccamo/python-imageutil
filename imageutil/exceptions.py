__all__ = [
    "InvalidAnchorError",
    "InvalidColorError",
    "InvalidImageError",
]


class InvalidAnchorError(ValueError):
    """
    This class describes an invalid anchor error.
    """

    def __init__(self, anchor):
        message = (
            "Invalid anchor, expected a value between ("
            "'bottom', 'bottom-left', 'bottom-right', 'center', 'left', 'right', "
            f"'top', 'top-left', 'top-right'), found {anchor}."
        )
        super().__init__(message)


class InvalidColorError(ValueError):
    """
    This class describes an invalid opacity error.
    """

    def __init__(self, color):
        message = f"Invalid color, expected an RGB/RGBA color tuple, found {color}."
        super().__init__(message)


class InvalidImageError(ValueError):
    """
    This class describes an invalid image error.
    """

    def __init__(self, image):
        message = (
            f"Invalid image, expected an image filepath or a PIL image, found {image}."
        )
        super().__init__(message)
