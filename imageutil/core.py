from __future__ import annotations

from typing import Any

from imageutil import operations
from imageutil.args import get_image
from imageutil.pil import PILImageObject
from imageutil.types import ImageIn

__all__ = [
    "Image",
]


class Image:
    @classmethod
    def open(cls, src: ImageIn) -> Image:
        return cls(src)

    def __init__(self, src: ImageIn, copy: bool = True):
        self.pil_image = get_image(src, copy=copy)

    def __enter__(self) -> Image:
        return self

    def __exit__(self, e_type: str, e_value: Any, e_traceback: str) -> None:
        self.close()

    def __getattr__(self, attr: str) -> Any:
        try:
            value = getattr(operations, attr)
            return _ImageOperationAttr(self, value)
        except AttributeError:
            value = getattr(self.pil_image, attr)
            if callable(value):
                return _PILImageMethodAttr(self, value)
            return _PILImagePropertyAttr(self, value)()


class _ImageAbstractAttr:
    def __init__(self, image: Image, attr: Any):
        self._image = image
        self._attr = attr

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        value = self._get_value(*args, **kwargs)
        if isinstance(value, PILImageObject):
            self._image.pil_image = value
            return self._image
        elif value is None:
            return self._image
        return value

    def _get_value(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError()


class _ImageOperationAttr(_ImageAbstractAttr):
    def _get_value(self, *args: Any, **kwargs: Any) -> Any:
        return self._attr(self._image.pil_image, *args, **kwargs)


class _PILImageMethodAttr(_ImageAbstractAttr):
    def _get_value(self, *args: Any, **kwargs: Any) -> Any:
        return self._attr(*args, **kwargs)


class _PILImagePropertyAttr(_ImageAbstractAttr):
    def _get_value(self, *args: Any, **kwargs: Any) -> Any:
        return self._attr
