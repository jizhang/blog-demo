from typing import TypedDict

class Point(TypedDict):
    x: int
    y: int

p1: Point = {'x': 1, 'y': 2}
p2 = Point(x=1, y=2)
