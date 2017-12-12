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
import turtle
import math


class PacMan:       # creates the pacman class

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
