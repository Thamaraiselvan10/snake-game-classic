from turtle import Turtle,Screen
# declaring global variable
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
sn = Screen() # Creating object for Screen class
class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        sn.setup(width=600, height=600)
        sn.bgcolor("black")
        sn.title("Python game using python")
        sn.tracer(0)

    def update(self):
        sn.update()

    def exit(self):
        sn.exitonclick()

    def create_snake(self):
        """
        creating a snake with the three blocks
        """
        for pos in STARTING_POSITIONS:
           self.add_segment(pos)

    def listen_snake_move(self):
        #listening to the user's moves form their keys
        sn.listen()
        sn.onkey(key="Up", fun=self.up)
        sn.onkey(key="Down", fun=self.down)
        sn.onkey(key="Left", fun=self.left)
        sn.onkey(key="Right", fun=self.right)

    def move(self):
        # moving all the blocks which is followed by the head turtle
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[seg_num - 1].xcor()
            y_pos = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_pos, y_pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self,pos):
        #adding a new block everytime if the snake eats food
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())

