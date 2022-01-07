from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard


screen = Screen()

# Basic black screen of game getting created
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake game")

# Scoreboard obj created its init method will create the above title and score thing appearing at top centre
scoreboard = Scoreboard()
# Food obj is created its init method will create the blue dot i.e. turtle
food = Food()
# Snake obj is created its init will create snake
snake = Snake()
# All the created things will get updated at once
# screen.update()

# Listening all the arrow keys for doing the movement of snake
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


# Actual game loop going on it will go on until collision occurs
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision from food
    if snake.head.distance(food) < 15:
        food.refresh()
        # Calling score function of scoreboard which will update the score and write it down each time collision happens
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with snake body i.e. any of its segment colliding with its head
    for segment in snake.segments:
        # The head or the first segment will be at zero distance from itself so removing that case
        if segment == snake.head:
            pass
        # Else if it is not a head and has distance less than 10 from any other segments game over
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
