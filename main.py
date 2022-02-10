import time
from turtle import Screen

from car_manager import CarManager
import player
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
user = player.Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(user.player_move, "Up")
    car_manager.create_cars()
    speed = car_manager.car_movement()
    if user.ycor() > 280:
        user.player_start()
        car_manager.increase_speed()
        scoreboard.increase_level()
    for car in car_manager.all_cars:
        if car.distance(user) < 20:
            game_is_on = False
