from turtle import Turtle
import random as rd
class Food(Turtle):
    
    def __init__(self):
        """
        creating a food element in the game
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.food_pos()

    def eat(self):
        self.food_pos() #triggering this function when ever the snake touches the food
        
    def food_pos(self):
        #place the food in the random place within the canva
        rand_x = rd.randint(-280, 280)
        rand_y = rd.randint(-280, 280)
        self.goto(rand_x, rand_y)