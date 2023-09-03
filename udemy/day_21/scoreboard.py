from turtle import Turtle


class ScorerBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("White")
        self.hideturtle()
        self.setposition(0, 275)
        self.score = 0
        self.update_score(0)

    def update_score(self, point):
        self.score += point
        self.clear()
        self.write(f"Score: {self.score}", False, align='center', font=('Arial', 12, 'normal'))
