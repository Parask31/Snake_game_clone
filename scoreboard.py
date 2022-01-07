from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    # Initializes the score thing at top centre of game using write function of turtle
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.current_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.current_score}", False, align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()


