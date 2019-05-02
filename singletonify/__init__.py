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
from threading import RLock


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
    assert YourClass() is YourClass()
    ```

    `args` and `kwargs` will pass to ctor of `X` as args.
    '''

    def decorator(cls: type) -> Callable[[], object]:

        box = _Box()
        factory = None
        lock = RLock()

        def metaclass_call(_):
            if box.value is None:
                with lock:
                    if box.value is None:
                        instance = cls.__new__(factory, *args, **kwargs)
                        if isinstance(instance, factory):
                            cls.__init__(instance, *args, **kwargs)
                        box.value = (instance, ) # use tuple to handle `cls()` return `None`
            return box.value[0]

        def _is_init(*_):
            return box.value is not None

        SingletonMetaClass = type('SingletonMetaClass', (type(cls), ), {
            '__slots__': (),
            '__call__': metaclass_call
        })

        def __init_subclass__(cls, *args, **kwargs):
            raise TypeError('cannot inherit from a singleton class')

        factory = SingletonMetaClass(cls.__name__, (cls, ), {
            '__slots__': (),
            '__init_subclass__': __init_subclass__,
            '_is_init': _is_init,
        })
        return update_wrapper(factory, cls, updated=())

    return decorator
