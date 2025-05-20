import functools
from typing import *

from normed import _utils

__all__ = ["getclass", "getdecorator"]


def getclass(norm: Callable, /, *args: Any, **kwargs: Any) -> type:
    "This decorator turns a norm function into a normed class."
    Ans: type = _utils.getclass(norm, *args, **kwargs)
    Ans.__doc__ = _utils.getdoc(norm.__doc__)
    Ans.__module__ = str(norm.__module__)
    Ans.__name__ = str(norm.__name__)
    Ans.__qualname__ = str(norm.__qualname__)
    Ans.__new__.__annotations__ = _utils.getannotations(norm)
    Ans.__new__.__signature__ = _utils.getsignature(norm)
    Ans.__new__.__type_params__ = _utils.getparams(norm)
    return Ans


def getdecorator(*args: Any, **kwargs: Any) -> functools.partial:
    "This function returns a decorator."
    return functools.partial(getclass, *args, **kwargs)
