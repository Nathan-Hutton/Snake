from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.speed = 0.1


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        body_part = Turtle("square")
        body_part.color("white")
        body_part.penup()
        body_part.goto(position)
        self.segments.append(body_part)


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def move(self):
        time.sleep(self.speed)

        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].position())
        self.head.forward(MOVE_DISTANCE)


    def wall_collision(self):
        if -300 > self.head.xcor() or self.head.xcor() > 285:
            return True
        if -295 > self.head.ycor() or self.head.ycor() > 305:
            return True
        return False


    def tail_collision(self):
        for segment in self.segments[1:]:
            if segment.distance(self.head) < 10:
                return True
        return False


    def increase_speed(self):
        self.speed /= 1.05

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.speed = 0.1
        self.create_snake()
        self.head = self.segments[0]

