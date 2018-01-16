
singletonify
============

install
-------

.. code-block:: cmd

   pip install singletonify

usage
-----

.. code-block:: py

   @singleton
   class YourClass:
       pass

   assert YourClass() is YourClass()

why not other
-------------

There are many singleton libraries on pypi, but their all has problem:


* `singleton <https://pypi.python.org/pypi/singleton>`_ - cannot use ``issubclass()`` or ``__mro__`` or ...
* `singleton-decorator <https://pypi.python.org/pypi/singleton-decorator>`_ - cannot use ``isinstance()`` .
* `singleton_factory <https://pypi.python.org/pypi/singleton_factory>`_ - wtf, why do people use ``dict()[hash(obj)] = obj`` ?
* `singletonmetaclasss <https://pypi.python.org/pypi/singletonmetaclasss/0.1>`_ - a little like this, but not a decorator.
* `singleton3 <https://pypi.python.org/pypi/singleton3>`_ - haha
* `pysingleton <https://pypi.python.org/pypi/pysingleton>`_ - ABANDONED.
