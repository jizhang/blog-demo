from typing import TypeVar, Generic

T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def set(self, new: T):
        print(f'Set value to {new}, previous value is {self.value}')
        self.value = new


v = LoggedVar[int](1)
v.set(2)
