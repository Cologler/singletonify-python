#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from abc import abstractmethod
from typing import Callable
from functools import update_wrapper
import threading

class _SingletonBase:
    __slots__ = ()


class _Box:
    __slots__ = ('value')
    def __init__(self):
        self.value = None


def singleton(*args, **kwargs):
    '''
    a lazy init singleton pattern.

    usage:

    ``` py
    @singleton()
    class X: ...
    ```

    `args` and `kwargs` will pass to ctor of `X` as args.
    '''

    def decorator(cls: type) -> Callable[[], object]:
        if issubclass(cls, _SingletonBase):
            raise TypeError('cannot inherit from another singleton class.')

        box = _Box()
        factory = None

        def metaclass_call(_):
            if box.value is None:
                instance = cls(*args, **kwargs)
                instance.__class__ = factory
                box.value = (instance, ) # use tuple to handle `cls()` return `None`
            return box.value[0]

        SingletonMetaClass = type('SingletonMetaClass', (type(cls), ), {
            '__slots__': (),
            '__call__': metaclass_call
        })

        factory = SingletonMetaClass(cls.__name__, (cls, _SingletonBase), {
            '__slots__': (),
        })
        return update_wrapper(factory, cls, updated=())

    return decorator
