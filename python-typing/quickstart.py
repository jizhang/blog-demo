# Function argument and return value
def greeting(name: str) -> str:
    return 'hello ' + name

def greeting(name: str) -> str:
    real_name = name + 1
    return 'hello ' + real_name

greeting(1)
greeting('world') + 1


# Local variable
def greeting(name: str) -> str:
    real_name = 'hello ' + name
    number: int = real_name
    return number


# Collection types
items: list = 0

nums: list[int] = []
nums.append('text')

ages: dict[str, int] = {}
ages['John'] = '30'


# Class
class Job:
    suffix: str

    def __init__(self, date: str, suffix: str):
        self.date = date

    def run(self) -> None:
        self.date + 1
        self.suffix + 1
