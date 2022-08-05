import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(fun=player.move, key="w")

car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create()
    car_manager.move_cars()

    if player.distance(0, 300) <= 10:
        player.reset()
        scoreboard.next_level()
        car_manager.move_increase()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            screen.clear()
            scoreboard.end()

screen.exitonclick()