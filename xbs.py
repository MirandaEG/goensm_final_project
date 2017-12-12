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
import random


class Xps:

    def __init__(self, game):
        self.game = game
        self.tess = turtle.Turtle()
        self.x = random.randint(-480, 460)
        self.y = random.randint(-305, 150)
        self.setup()


    def setup(self):
        self.tess.penup()
        self.tess.color('white')
        self.tess.pensize(1)
        self.tess.goto(self.x, self.y)
        self.tess.speed(100)
        self.tess.shape('triangle')
        self.tess.showturtle()

    # def move_position(self):
    #     self.tess.goto(random.randint(-100, 100), random.randint(-100, 100))

    def hide(self):
            #print("We touched!")
            self.tess.hideturtle()
            self.tess.reset()       #  resets the turtle to its regular state
            self.game.points = Xps(self.game)       # calls the object again.


    # def show(self):
    #     self.tess.showturtle()
