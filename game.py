import math
from pacman import *
from xbs import *


class Game:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("TurtleMan")
        self.wn.bgcolor('black')
        self.pacman = PacMan(self)
        self.points = Xps(self)
        self.make_border()\
        # self.test_length_bord()

        # while True:
        self.wn.onkey(self.pacman.forward, "Up")
        self.wn.onkey(self.pacman.right,  "Right")
        self.wn.onkey(self.pacman.left, "Left")
        self.wn.listen()

        # use the distance formula to determine the distance between pacman turtle and the point turtle. Once the pacman turtle gets close hide the point turtle.

            # spawn new point
            # points.show()
    # get the turtle to turn 180 degrees when it hits the borders.

        self.wn.mainloop()

    # def test_length_bord(self):
    #     test = turtle.Turtle()
    #     test.pendown()
    #     test.left(90)
    #     test.forward(175)
    #     test.color('red')

    def make_border(self):
        border = turtle.Turtle()
        border.penup()
        border.pensize(7)
        border.goto(-500, -325)
        border.color('blue')
        border.pendown()
        for i in range(2):
            border.fd(980)
            border.lt(90)
            border.fd(500)
            border.lt(90)

    def turn(self):
        if self.pacman.turt.xcor() > 460 or self.pacman.turt.xcor() < -480:
           self.pacman.turt.right(180)
        if self.pacman.turt.ycor() > 150 or self.pacman.turt.ycor() < -305:
           self.pacman.turt.right(180)

    def check_distance(self):

        distance = math.sqrt(math.pow(self.pacman.turt.xcor() - self.points.tess.xcor(), 2) + math.pow(self.pacman.turt.ycor() - self.points.tess.ycor(), 2))
        # print(distance)
        if distance < 20:
            self.points.hide()

def main():

    g = Game()

main()
