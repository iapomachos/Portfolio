from turtle import Turtle

#I had to import pathlib since relative paths weren't working on windows (os.getcwd() was showing my home directory)
#related stackoverflow article: https://stackoverflow.com/questions/71811330/python-searching-for-image-in-wrong-directory
import pathlib

#Scoreboard's score constant parameters
ALIGN = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(pathlib.Path(__file__).parent / "high_score_keeper.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()
       

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGN, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(pathlib.Path(__file__).parent / "high_score_keeper.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
        
       