#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from abc import abstractmethod
import threading

class _SingletonBase:
    __slots__ = ()

    @abstractmethod
    def new(self, *args, **kwargs):
        pass


def singleton(*args):

    lock = threading.RLock()
    instance = lock

    def new_singleton_metaclass(_type):
        class Singleton(_type, _SingletonBase):
            __slots__ = ()

            def __call__(self, *args, **kwargs):
                nonlocal instance
                if instance is lock:
                    with lock:
                        if instance is lock:
                            if issubclass(_type, _SingletonBase):
                                instance = _type.new(self, *args, **kwargs)
                            else:
                                instance = self.new(*args, **kwargs)
                return instance

            def new(self, *args, **kwargs):
                return super().__call__(*args, **kwargs)

        return Singleton

    def _wrap(cls):
        metaclass = new_singleton_metaclass(type(cls))

        # pylint: disable=E1139
        class WrapedClass(cls, metaclass=metaclass):
            __slots__ = ()

        for attr in ('__module__', '__name__', '__qualname__', '__doc__'):
            setattr(WrapedClass, attr, getattr(cls, attr))

        return WrapedClass

    if args:
        cls, = args
        return _wrap(cls)
    else:
        return _wrap
