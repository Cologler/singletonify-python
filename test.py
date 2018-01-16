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

    def test_with_slots(self):
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
            def __init__(self):
                self.a = 1

        @singleton
        class Class2(Class1):
            def __init__(self):
                super().__init__()
                self.a = 2
                self.b = 'b'

        self.assertIs(Class1(), Class1())
        self.assertIs(Class2(), Class2())
        self.assertIsNot(Class1(), Class2())
        self.assertIsInstance(Class1(), Class1)
        self.assertIsInstance(Class2(), Class1)
        self.assertIsInstance(Class2(), Class2)
        self.assertNotIsInstance(Class1(), Class2)

        self.assertEqual(Class1().a, 1)
        self.assertEqual(Class2().a, 2)
        self.assertEqual(Class2().b, 'b')


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        unittest.main()
    except Exception:
        traceback.print_exc()

if __name__ == '__main__':
    main()
