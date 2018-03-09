"""
a coworker found a terrifying bit in the codebase where a class passed its
self.__dict__ into another class making for unpredictable behabior

i was inspired to try and create something equally evil
"""
import random


class Gallant(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)


class Goofus(object):
    def __init__(self, **kwargs):
        keys = kwargs.keys()
        vals = kwargs.values()
        random.shuffle(keys)
        random.shuffle(vals)
        for k, v in zip(keys, vals):
            setattr(self, k, v)

    def __dict__(self):
        return 'fuck your introspection'

    def __getattribute__(self, k):
        var = object.__getattribute__(self, k)
        if random.choice([True, False]):
            object.__setattr__(self, k, random.randint(1, 10))
        return var

    def __getattr__(self, k):
        var = object.__getattr__(self, k)
        if random.choice([True, False]):
            object.__setattr__(self, k, random.randint(1, 10))
        return var
