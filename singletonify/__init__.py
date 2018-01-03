#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import threading

class _EmptyLock:
    def __enter__(self):
        pass
    def __exit__(self, *args, **kwargs):
        pass
_NULL_LOCK = _EmptyLock()


def singleton(*args, namespace={}, concurrent=False):

    lock = _NULL_LOCK if not concurrent else threading.RLock()

    def new_singleton_metaclass(_type):
        class Singleton(_type):
            __slots__ = ()

            def __call__(self, *args, **kwargs):
                with lock:
                    if self not in namespace:
                        namespace[self] = super().__call__(*args, **kwargs)
                    return namespace[self]
        return Singleton

    def _wrap(cls):
        with lock:
            metaclass = namespace.get(0)
            if metaclass is None:
                namespace[0] = metaclass = new_singleton_metaclass(type)

        if type(cls) not in (type, metaclass):
            metaclass = new_singleton_metaclass(type(cls))

        # pylint: disable=E1139
        class WrapedClass(cls, metaclass=metaclass):
            __slots__ = ()

        for attr in ('__module__', '__name__', '__qualname__', '__doc__'):
            setattr(WrapedClass, attr, getattr(cls, attr))

        return WrapedClass

    _wrap.clear_cache = namespace.clear
    _wrap.get = namespace.get

    if args:
        cls, = args
        return _wrap(cls)
    else:
        return _wrap
