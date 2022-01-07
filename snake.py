from turtle import Turtle

body_position = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # Initializes the three squared snake body as soon as object of these snake class is created.
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Creates three squared segments of snake initially at start.
        for position in body_position:
            self.add_segment(position)

    def add_segment(self, position):
        # Adds new segment to snake at given position.
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Adds a new segment to snake via calling the add segment and passing last segments position to snake.
        self.add_segment(self.segments[-1].position())

    def move(self):
        # The last segment moves to second last in first loop and second last moves to first in second loop.
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Finally, moving the head or first segment ahead.
        self.head.forward(MOVE_DISTANCE)

    # Movements of snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
