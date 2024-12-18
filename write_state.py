from turtle import Turtle
ALIGN = 'center'
FONT = ('Constantia', 14, 'normal')

class WriteState(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()

    def move_and_write(self, name, x_pos, y_pos):
        self.goto(x_pos, y_pos)
        self.write(name, move=False, align=ALIGN, font=FONT)
