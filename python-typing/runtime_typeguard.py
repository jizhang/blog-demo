from collections.abc import Sequence

from typeguard import typechecked


class Animal: ...
class Cat(Animal): ...


@typechecked
def some_function(animals: Sequence[Animal]):
    pass


cats = [Cat()]
some_function(cats)
some_function([1])
