import random

board_width = 40


class Game():

    def checkIfGameOver(self):
        # If head touches wall, set output to True
        # How to deal with start @ (0, 0) ?
        if self.snakeObject.body_list[0].x >= board_width or self.snakeObject.body_list[0].x <= 0:
            return True
        if self.snakeObject.body_List[0].y >= board_width or self.snakeObject.body_List[0].y <= board_width:
            return True
        # If snake intersects itself, set output to True
        if self.snakeObject.body_List[0].x == "matching x coordinate in dictionary" and self.snakeObject.body_List[0].y == "matching y coordinate in dictionary":
            return True

    def __init__(self):
        self.snakeObject = Snake()
        self.score = 0

        x = random.randint(1, board_width)
        y = random.randint(1, board_width)

        self.food_coordinate = (x, y)

    def MainGameLoop(self, input):

        # MIGHT HAVE TO REWRITE THIS VVVVVVVVVVV

        # instead of replacing the head
        # add a new coordinate to the front of the list

        if (input == "up"):
            self.snakeObject.direction = "up"
            x = self.snakeObject.body_List[0].x
            y = self.snakeObject.body_List[0].y
            # If head coordinates overlap with food, prepend coordinates to list
            if self.food_coordinate(x, y) == self.snakeObject.body_List[0]:
                self.snakeObject.body_List.insert(0, (x, y + 1))
            else:
                # If did not eat food, prepend coordinates then delete last item in list
                self.snakeObject.body_List.insert(0, (x, y + 1))
                self.snakeObject.body_List.remove(-1, (x, y))

        if (input == "left"):
            self.snakeObject.direction = "left"
            self.snakeObject.body_List[0] = dict(
                x=self.snakeObject.body_List[0].x - 1, y=self.snakeObject.body_List[0].y)
        if (input == "down"):
            self.snakeObject.direction = "down"
            self.snakeObject.body_List[0] = dict(
                x=self.snakeObject.body_List[0].x, y=self.snakeObject.body_List[0].y - 1)
        if (input == "right"):
            self.snakeObject.direction = "right"
            self.snakeObject.body_List[0] = dict(
                x=self.snakeObject.body_List[0].x + 1, y=self.snakeObject.body_List[0].y)

            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        # If we didnt eat an apple; delete the last item in the list of coordinates


class Snake():
    def __init__(self):
        self.body_List = [dict(
            x=0,
            y=0
        )]
        self.direction = "down"


g = Game()
while (not g.isGameOver):
    g.MainGameLoop()
