from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.pu()
        self.reset()
        self.seth(90)

    
    def reset(self):
        '''Spawns turtle at starting position'''
        self.goto(STARTING_POSITION)
    
    
    def move(self):
        ''' Moves the turtle forward'''
        self.fd(MOVE_DISTANCE)


    def successful_cross(self):
        '''Checks if the turtle has successfully crossed the road
        @return True if the turtle has successfully crossed the road
        @return False otherwise'''
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False