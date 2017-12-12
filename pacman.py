import turtle
import math


class PacMan:

    def __init__(self, game):
        self.game = game
        self.turt = turtle.Turtle()
        self.x = self.turt.xcor()
        self.y = self.turt.ycor()
        self.set_up()

    def set_up(self):
        self.turt.shape('turtle')
        self.turt.penup()
        self.turt.color('yellow')
        self.turt.goto(0, -45)

    def forward(self):
        self.turt.forward(10)
        self.game.check_distance()
        self.game.turn()

    def left(self):
        self.turt.left(90)

    def right(self):
        self.turt.right(90)
