import random

board_width = 40


class Game():

    def checkIfGameOver():
        return  # CHANGE

    def __init__(self):
        self.snakeObject = Snake()
        self.score = 0

        x = random.randint(1, board_width)
        y = random.randint(1, board_width)

        self.food_coordinate = (x, y)

    def MainGameLoop(self, input):
        if (input == "up"):
            self.snakeObject.direction = "up"
            self.snakeObject.body_List[0] = dict(
                x=self.snakeObject.body_List[0].x, y=self.snakeObject.body_List[0].y + 1)
        if (input == "left"):
            self.snakeObject.direction = "left"
            self.snakeObject.body_List[0] = dict(
                x=self.snakeObject.body_List[0].x, y=self.snakeObject.body_List[0].y - 1)
        if (input == "down"):
            self.snakeObject.direction = "down"
            self.snakeObject.body_List[0] = dict(
                x=self.snakeObject.body_List[0].x + 1, y=self.snakeObject.body_List[0].y)
        if (input == "right"):
            self.snakeObject.direction = "right"
            self.snakeObject.body_List[0] = dict(
                x=self.snakeObject.body_List[0].x - 1, y=self.snakeObject.body_List[0].y)


class Snake():
    def __init__(self):
        self.body_List = [{0, 0}]
        self.direction = "down"


g = Game()
while (not g.isGameOver):
    g.MainGameLoop()
