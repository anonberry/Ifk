from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 25, "normal")


class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)