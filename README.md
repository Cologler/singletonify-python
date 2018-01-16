# singletonify

## install

``` cmd
pip install singletonify
```

## usage

``` py
@singleton
class YourClass:
    pass

assert YourClass() is YourClass()
```

## why not other

There are many singleton libraries on pypi, but their all has problem:

* [singleton](https://pypi.python.org/pypi/singleton) - cannot use `issubclass()` or `__mro__` or ...
* [singleton-decorator](https://pypi.python.org/pypi/singleton-decorator) - cannot use `isinstance()` .
* [singleton_factory](https://pypi.python.org/pypi/singleton_factory) - wtf, why do people use `dict()[hash(obj)] = obj` ?
* [singletonmetaclasss](https://pypi.python.org/pypi/singletonmetaclasss/0.1) - a little like this, but not a decorator.
* [singleton3](https://pypi.python.org/pypi/singleton3) - haha
* [pysingleton](https://pypi.python.org/pypi/pysingleton) - ABANDONED.
