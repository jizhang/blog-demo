from typing import TypeVar
from collections.abc import Sized

T = TypeVar('T', bound=Sized)

def longer(x: T, y: T) -> T:
    if len(x) > len(y):
        return x
    return y

print(longer([1], [1, 2]))
print(longer([1], {1, 2}))
print(longer([1], 'ab'))
