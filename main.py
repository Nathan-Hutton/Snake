from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.tracer(0)
screen.setup(600, 600, starty=0)

screen.bgcolor("black")
screen.title("Snake game")

while True:
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        snake.increase_speed()
    if snake.tail_collision() or snake.wall_collision():
        scoreboard.reset()
        snake.reset()

screen.exitonclick()

