from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        """
        creating score text in the turtle canva
        """
        super().__init__()
        self.penup()
        self.score=0
        self.color("white")
        self.goto(0, 260)
        self.write_score()
        self.hideturtle()

    def write_score(self):
        """
        Writing the score at first time
        """
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def update_score(self):
        """
        updating the user score
        """
        self.score+=1
        self.clear() # clearing the previous first score entry in the scoreboard
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))

    def game_over(self):
        """
        printing game over text at the middle of the canva
        """
        self.goto(0,0)
        self.write("game over",align="center",font=("Arial",54,"normal"))