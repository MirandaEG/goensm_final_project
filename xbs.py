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
            self.tess.reset()
            self.game.points = Xps(self.game)


    # def show(self):
    #     self.tess.showturtle()
