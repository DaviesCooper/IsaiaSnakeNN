import random
from snakeObject import Snake, Direction, Coordinate

# MAKE IT SO THE APPLE CHANGES LOCATION WHEN EATEN
# FIX CONSOLE BUG



class Game():
    
    def __init__(self, dimension):
        self.dimension = dimension
        dimension = 20
        self.snakeObject = Snake()
        self.score = 0
        self.food_coordinate = Coordinate(random.randint(1, dimension), random.randint(1, dimension))




    def checkIfGameOver(self):
        # If head touches wall, set output to True
        # How to deal with start @ (0, 0) ?
        if self.snakeObject.body_List[0].x >= self.dimension or self.snakeObject.body_List[0].x < 0:
            return True
        if self.snakeObject.body_List[0].y >= self.dimension or self.snakeObject.body_List[0].y < 0:
            return True
        
        # If snake intersects itself, set output to True
        if self.snakeObject.body_List[0].x == "matching x coordinate in dictionary" and self.snakeObject.body_List[0].y == "matching y coordinate in dictionary":
            return True

    

    def MainGameLoop(self, input):
        print(input)
        #print food coordinates'F'
        print("Food is at x=", self.food_coordinate.x, "y=", self.food_coordinate.y)
        self.snakeObject.direction = input
        x = 0
        y = 0
        if (input == Direction.UP):
            x = self.snakeObject.body_List[0].x
            y = self.snakeObject.body_List[0].y-1       
        if (input == Direction.LEFT):
            x = self.snakeObject.body_List[0].x-1
            y = self.snakeObject.body_List[0].y  
        if (input == Direction.DOWN):
            x = self.snakeObject.body_List[0].x
            y = self.snakeObject.body_List[0].y+1  
        if (input == Direction.RIGHT):
            x = self.snakeObject.body_List[0].x+1
            y = self.snakeObject.body_List[0].y  

        # If head coordinates overlap with food,
        # prepend coordinates to list && change food location
        if self.food_coordinate.x == x and self.food_coordinate.y == y:
            self.snakeObject.body_List.insert(0, Coordinate(x, y))
            self.food_coordinate = Coordinate(random.randint(1, self.dimension), random.randint(1, self.dimension))

        else:
            # If did not eat food, prepend coordinates then delete last item in list
            self.snakeObject.body_List.insert(0, Coordinate(x, y))
            self.snakeObject.body_List = self.snakeObject.body_List[:-1]


    def printToConsole(self):
        board = [[0 for col in range(self.dimension)] for row in range(self.dimension)]
        for coordinate in self.snakeObject.body_List:
            board[coordinate.y][coordinate.x] = "S"
        board[self.food_coordinate.y][self.food_coordinate.x] = "F"
        for row in board:
            print(row)
        


g = Game(20)
while (not g.checkIfGameOver()):
    dir = Direction.RIGHT
    move = input()
    match move:
        case "up":
            dir = Direction.UP
        case "right":
            dir = Direction.RIGHT
        case "down":
            dir = Direction.DOWN
        case "left":
            dir = Direction.LEFT
        case _:
            dir = g.snakeObject.direction
    g.MainGameLoop(dir)
    g.printToConsole()
    