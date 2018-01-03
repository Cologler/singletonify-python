#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import sys
import traceback
import unittest
from singletonify import singleton


class Test(unittest.TestCase):
    def test_singleton(self):
        @singleton
        class Class1:
            pass

        @singleton
        class Class2:
            pass

        self.assertIs(Class1(), Class1())
        self.assertIs(Class2(), Class2())
        self.assertIsNot(Class1(), Class2())

    def test_slots(self):
        @singleton
        class SingletonClassWithDict:
            pass

        @singleton
        class SingletonClassWithSlots:
            __slots__ = ('buffer', )

        self.assertTrue(hasattr(SingletonClassWithDict(), '__dict__'))
        self.assertFalse(hasattr(SingletonClassWithSlots(), '__dict__'))

    def test_inherit(self):
        @singleton
        class Class1:
            pass

        @singleton
        class Class2(Class1):
            pass

        self.assertIsNot(Class1(), Class2())
        self.assertIsInstance(Class2(), Class1)


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        unittest.main()
    except Exception:
        traceback.print_exc()

if __name__ == '__main__':
    main()
