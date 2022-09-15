
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    # move turtle
    screen.listen()
    screen.onkeypress(player.move, 'Up')
    car_manager.create_car()
    car_manager.move()

    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.end_of_game()

    # detect successful crossing
    if player.successful_cross():
        player.reset()
        scoreboard.update_level()
        car_manager.level_up()


screen.exitonclick()
