from PIL import Image as PILImage
from PIL import ImageFile as PILImageFile
from PIL.Image import Image as PILImageObject

__all__ = [
    "PILImage",
    "PILImageFile",
    "PILImageObject",
]

PILImageFile.MAXBLOCK = 1024 * 1024
