#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from abc import abstractmethod
from functools import update_wrapper
import threading

class _SingletonBase:
    __slots__ = ()

    @abstractmethod
    def new(self, *args, **kwargs):
        pass


def singleton(cls):

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

    metaclass = new_singleton_metaclass(type(cls))

    # pylint: disable=E1139
    class WrapedClass(cls, metaclass=metaclass):
        __slots__ = ()

    update_wrapper(WrapedClass, cls, updated=())

    return WrapedClass
