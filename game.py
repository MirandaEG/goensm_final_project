######################################################################
# Author: Miranda Goens
# Username:goensm
#
# Assignment: Final Project
#
# Purpose: To show my learning experience in the class, implement code, and to improve problem solving skills.
######################################################################
# Acknowledgements:
#
# Dr. Heggen
# helped me on the main code which is the game class.
#Christian Thompson
#https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg
# Google, pacman game
#https://www.google.com/search?source=hp&ei=pEsvWqjtOYaYjwTI4J2oBA&q=pacman+game+free&oq=pacman+game+free&gs_l=psy-ab.3..0l10.1621.4380.0.4608.17.14.0.0.0.0.344.1960.0j6j3j1.10.0....0...1c.1.64.psy-ab..7.10.1958.0..35i39k1j0i67k1j0i131k1j0i10i67k1j0i20i264k1j0i10k1.0.zioeUUCwfuQ
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################
import math
from pacman import *
from xbs import *


class Game:
    def __init__(self): # initializes objects and windows
        self.wn = turtle.Screen()
        self.wn.title("TurtleMan")
        self.wn.bgcolor('black')
        self.pacman = PacMan(self)
        self.points = Xps(self)
        self.make_border()\
        # self.test_length_bord()

        # while True:
        self.wn.onkey(self.pacman.forward, "Up")    #creates the up arrow key to move the turtle forward
        self.wn.onkey(self.pacman.right,  "Right")  #creates the right arrow key to turn the turtle right
        self.wn.onkey(self.pacman.left, "Left")     #creates the left arrow key to turn the turtle left
        self.wn.listen()

        # use the distance formula to determine the distance between pacman turtle and the point turtle. Once the pacman turtle gets close hide the point turtle.

            # spawn new point
            # points.show()
    # get the turtle to turn 180 degrees when it hits the borders.

        self.wn.mainloop()              # calls the onkey multiple times

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

    def turn(self):         #turns the turtle 180 degrees when the turtle hits the border.
        if self.pacman.turt.xcor() > 460 or self.pacman.turt.xcor() < -480:
           self.pacman.turt.right(180)
        if self.pacman.turt.ycor() > 150 or self.pacman.turt.ycor() < -305:
           self.pacman.turt.right(180)

    def check_distance(self):           # defines the distance between the pacman turtle and point turtle

        distance = math.sqrt(math.pow(self.pacman.turt.xcor() - self.points.tess.xcor(), 2) + math.pow(self.pacman.turt.ycor() - self.points.tess.ycor(), 2))
        # print(distance)
        if distance < 20:
            self.points.hide()      # hides the point turtle and then moves the point turtle randomly.

def main():

    g = Game()          # define the game

main()      # calls the game
