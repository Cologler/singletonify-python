#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from pytest import raises

from singletonify import singleton


def test_base():
    @singleton()
    class A:
        pass
    assert A() is A()

def test_with_args():
    @singleton(x='s')
    class A:
        def __init__(self, x):
            self.x = x
    assert A() is A()
    assert A().x == 's'

def test_instance_check():
    @singleton()
    class A:
        pass
    assert isinstance(A(), A)

def test_subclass_check():
    class B:
        pass

    @singleton()
    class A(B):
        pass

    assert issubclass(A, B)

def test_multi_apply():
    @singleton()
    class A:
        pass

    @singleton()
    class B:
        pass

    assert A() is A()
    assert B() is B()
    assert A() is not B()

def test_with_slots():
    @singleton()
    class D:
        pass

    @singleton()
    class S:
        __slots__ = ('buffer', )

    assert hasattr(D(), '__dict__')
    assert not hasattr(S(), '__dict__')

def test_inherit():
    class B:
        pass

    @singleton()
    class A(B):
        pass

    assert A() is A()
    assert B() is not B()
    assert A() is not B()
    assert type(A()) is A
    assert isinstance(A(), A)

def test_inherit_from_singleton():
    @singleton()
    class B:
        pass

    # cannot inherit
    with raises(TypeError):
        @singleton()
        class A(B):
            pass
