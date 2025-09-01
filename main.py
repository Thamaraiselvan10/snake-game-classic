from turtle import Turtle,Screen
from food import Food
from score_board import Scoreboard
import time
from Snake import Snake

snake=Snake() # creating object for Snake class
food=Food() # Creating object for Food class
snake.listen_snake_move() # listening to the user's moves from the keys
score=Scoreboard()
game_is_on=True
while game_is_on:

    snake.update()
    # Make it go more slowly until it eats five fruits
    if len(snake.segments)==10:
        time.sleep(0.2)
    else:
        time.sleep(0.3)
    snake.move()
    #detect collision with food.
    if snake.head.distance(food)<15:
        food.eat()
        score.update_score()
        snake.extend()

    #Dectect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor() <-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        score.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            score.game_over()

snake.exit()