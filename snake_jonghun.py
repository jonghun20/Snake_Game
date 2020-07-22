from turtle import Turtle, Screen
import time
import random

class Gfx:
    def __init__(self):
        self.window = Screen()
        self.window.title("Snake Game")
        self.window.bgcolor("lightblue")
        self.window.setup(width=600, height=600)

    def start(self):
        self.window.mainloop()

class Food:
    def __init__(self):
        self.food = Turtle()
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.food.hideturtle()
        self.food.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.food.showturtle()
        self.food.speed(0)

        # while True:
        #     if self.head.distance(self.food) < 20:
        #         self.food.goto(random.randint(-280, 280), random.randint(-280, 280))

class Snake(Gfx):
    def __init__(self, x, y):
        super(Snake,self).__init__()
        self.x = x
        self.y = y
        self.head = Turtle()
        self.head.goto(0, 0)
        self.head.shape("square")
        self.head.color("green")
        self.head.penup()
        self.window.listen()
        self.keyboardPress()
        self.food_obj = Food()
        self.head.speed(10)

        self.body = []
        # self.create_new_body()
        # self.new_body = Turtle()
        # self.new_body.speed(0)
        # self.new_body.shape("square")
        # self.new_body.color("green")
        # self.new_body.penup()

        # Apple appears in a random place when snake is near
    def detectFood(self):
        if self.head.distance(self.food_obj.food) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            self.food_obj.food.goto(x, y)
            self.create_new_body()
            self.body.append(self.new_body)

    def create_new_body(self):
        self.new_body = Turtle()
        self.new_body.speed(0)
        self.new_body.shape("square")
        self.new_body.color("green")
        self.new_body.penup()

    def checkBody(self):
        for index in range(len(self.body) - 1, 0, -1):
            x = self.body[index - 1].xcor()
            y = self.body[index - 1].ycor()
            self.body[index].goto(x, y)

        if len(self.body) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.body[0].goto(x, y)

    def moveUp(self):
        while True:
            self.detectFood()
            y = self.head.ycor()
            self.head.sety(y + 20)
            time.sleep(0.1)
            self.checkBody()
            self.end()

    def moveDown(self):
        while True:
            self.detectFood()
            y = self.head.ycor()
            self.head.sety(y - 20)
            time.sleep(0.1)
            self.checkBody()
            self.end()

    def moveRight(self):
        while True:
            self.detectFood()
            x = self.head.xcor()
            self.head.setx(x + 20)
            time.sleep(0.1)
            self.checkBody()
            self.end()

    def moveLeft(self):
        while True:
            self.detectFood()
            x = self.head.xcor()
            self.head.setx(x - 20)
            time.sleep(0.1)
            self.checkBody()
            self.end()

    def keyboardPress(self):
        self.window.onkey(lambda: self.moveUp(), 'Up')
        self.window.onkey(lambda: self.moveRight(), 'Right')
        self.window.onkey(lambda: self.moveLeft(), 'Left')
        self.window.onkey(lambda: self.moveDown(), 'Down')

    def startOver(self):
        self.head.hideturtle()
        self.head.home()
        self.head.showturtle()

    def end(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            return self.startOver()

    # def food(self):
    #     self.food = Turtle()
    #     self.food.shape("circle")
    #     self.food.color("red")
    #     self.food.penup()
    #     self.food.hideturtle()
    #     self.food.goto(random.randint(-280, 280), random.randint(-280, 280))
    #     self.food.showturtle()
    #
    #     while True:
    #         if self.head.distance(self.food) < 20:
    #             self.food.goto(random.randint(-280, 280), random.randint(-280, 280))

# class Food:
#     def __init__(self):
#         self.food = Turtle()
#         self.food.shape("circle")
#         self.food.color("red")
#         self.food.penup()
#         self.food.hideturtle()
#         self.food.goto(random.randint(-280, 280), random.randint(-280, 280))
#         self.food.showturtle()
#
#         if self.head.distance(self.food) < 20:
#             self.food.goto(random.randint(-280, 280), random.randint(-280, 280))


Snake(0, 0).start()




