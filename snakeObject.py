
from enum import Enum

# class syntax

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Snake():
    def __init__(self):
        self.body_List = [Coordinate(1,0)]
        self.direction = Direction.DOWN