from typing import TypeVar
from collections.abc import Sequence

T = TypeVar('T')

def first(seq: Sequence[T]) -> T:
    return seq[0]

print(first([1, 2, 3]))
print(first('abc'))
