from typing import *

from normed import _utils

__all__ = ["getclass", "getdecorator"]


class Norming:
    def __init__(self: Self, /, *args: Any, **kwargs: Any) -> None:
        "This"
        self.args = args
        self.kwargs = kwargs

    def __call__(self: Self, norm: Callable) -> type:
        "This decorator turns a norm function into a normed class."
        Ans: type = _utils.getclass(norm, *self.args, **self.kwargs)
        Ans.__doc__ = _utils.getdoc(norm.__doc__)
        Ans.__module__ = str(norm.__module__)
        Ans.__name__ = str(norm.__name__)
        Ans.__qualname__ = str(norm.__qualname__)
        Ans.__new__.__annotations__ = _utils.getannotations(norm)
        Ans.__new__.__signature__ = _utils.getsignature(norm)
        Ans.__new__.__type_params__ = _utils.getparams(norm)
        return Ans
