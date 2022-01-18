from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    # Initializes the score thing at top centre of game using write function of turtle
    def __init__(self):
        super().__init__()
        with open("data.txt", mode='r') as data:
            self.high_score = int(data.read())
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.current_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.current_score} High score:{self.high_score}", False, align= ALIGNMENT, font= FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode='w') as file2:
                file2.write(str(self.high_score))
        self.current_score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.current_score += 1
        self.update_scoreboard()

