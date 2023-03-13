# initial import
from turtle import Screen
from player import Player
from block import Block
from scoreboard import ScoreBoard
import time

# screen part
main_screen = Screen()
main_screen.setup(600, 600)
main_screen.title("Cross the Road!!")

# animation part
main_screen.tracer(0)

# level (scoreboard part)
level = ScoreBoard()

# our little turtle
player = Player()

# listeners
main_screen.onkey(player.move, "space")
main_screen.listen()

# game instances
game_on = True
speed = 2
loop_num = 0
blocks = []

while game_on:
    loop_num += 1

    if loop_num % 6 == 0:
        new_block = Block()
        blocks.append(new_block)

    main_screen.update()
    time.sleep(0.1)

    for block in blocks:
        block.forward(speed)

        if player.collide(block):
            level.game_over()
            game_on = False

    if player.ycor() > 260:
        speed += 2
        level.update()
        player.passed()

# last part
main_screen.listen()
main_screen.exitonclick()
