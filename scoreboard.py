FONT = ("Courier", 16, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.ht()
        self.goto(0,275)
        self.write(f"Level {self.level}",False,'center', FONT)

    def next_level(self):
        self.clear()
        self.level +=1
        self.write(f"Level {self.level}",False,'center', FONT)

    def end(self):
        self.goto(0,0)
        self.write("GAME OVER",False, 'center',("Courier",30, "normal"))