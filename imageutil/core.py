from imageutil import operations
from imageutil.args import get_image
from imageutil.pil import PILImageObject
from imageutil.types import ImageIn

__all__ = [
    "Image",
]


class Image:
    @classmethod
    def open(cls, src: ImageIn):
        return cls(src)

    def __init__(self, src: ImageIn, copy: bool = True):
        self.pil_image = get_image(src, copy=copy)

    def __enter__(self):
        return self

    def __exit__(self, e_type, e_value, e_traceback):
        self.close()

    def __getattr__(self, attr: str):
        try:
            value = getattr(operations, attr)
            return _ImageOperationAttr(self, value)
        except AttributeError:
            value = getattr(self.pil_image, attr)
            if callable(value):
                return _PILImageMethodAttr(self, value)
            return _PILImagePropertyAttr(self, value)()


class _ImageAbstractAttr:
    def __init__(self, image, attr):
        self._image = image
        self._attr = attr

    def __call__(self, *args, **kwargs):
        value = self._get_value(*args, **kwargs)
        if isinstance(value, PILImageObject):
            self._image.pil_image = value
            return self._image
        elif value is None:
            return self._image
        return value

    def _get_value(self, *args, **kwargs):
        raise NotImplementedError()


class _ImageOperationAttr(_ImageAbstractAttr):
    def _get_value(self, *args, **kwargs):
        return self._attr(self._image.pil_image, *args, **kwargs)


class _PILImageMethodAttr(_ImageAbstractAttr):
    def _get_value(self, *args, **kwargs):
        return self._attr(*args, **kwargs)


class _PILImagePropertyAttr(_ImageAbstractAttr):
    def _get_value(self, *args, **kwargs):
        return self._attr
