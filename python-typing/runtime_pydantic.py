from pydantic import BaseModel


class Point(BaseModel):
    x: float
    y: float


p = Point(x='1.23', y='abc')
