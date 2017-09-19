'''
This snippet is to show how to monitor when an object is deleted

'''
from functools import lru_cache
class BigClass:
    pass
class Foo:
    def __init__(self):
        self.big = BigClass()
    @lru_cache(maxsize=16)
    def cached_method(self, x):
        return x + 5

    def __del__(self):
         print(id(self), 'died')

def fun():
    foo = Foo()
    print(foo.cached_method(10))
    print(foo.cached_method(10)) # use cache
    return 'something'

fun()
