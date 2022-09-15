
from turtle import Turtle


FONT = ("comic sans MS", 20, "normal")


class Scoreboard(Turtle):
    

    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.level = 1
        self.show_level()


    def show_level(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f'Level: {self.level}', align='left', font=FONT)

    
    def update_level(self):
        '''Increase the level by one'''
        self.level += 1
        self.show_level()


    def end_of_game(self):
        self.goto(0, 0)
        self.write('Game over', align='center', font=FONT)
