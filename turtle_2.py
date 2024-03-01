import turtle
from random import randint
import random

screen = turtle.Screen()
screen.bgcolor("bisque")
screen.title("turtle game")
FONT = ('Arial', 30, 'normal')
score = 0
game_over = False

# turtle list
turtle_list = []

# score turtle
score_turtle = turtle.Turtle()

# countdown turtle
countdown_turtle = turtle.Turtle()


def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height()/2
    y = top_height*0.9
    score_turtle.goto(0, y)
    score_turtle.write(f"Score: {score}", move=False,
                       align="center", font=FONT)


def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score: {score}",
                           move=False, align="center", font=FONT)
        # print(x, y)
    t.onclick(handle_click)
    t.penup()
    t.shape('turtle')
    t.shapesize(2, 2)
    t.color("dark green")
    t.goto(x*randint(-20, 20), y*randint(-20, 20))
    # bos turtle_list=[] dizisine bir üst satırda oluşturulanları ekliyoruz.
    turtle_list.append(t)


x_coordinates = random.sample(range(-20, 20), 5)
y_coordinates = random.sample(range(-20, 20), 4)


def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

# gizlenmiş turtlelardan random birini gösteren fonk
# recursive function: kendini sürekli çağırarak çalıştıracak.


def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

# recursive function


def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()

    top_height = screen.window_height()/2
    y = top_height*0.9
    countdown_turtle.goto(0, y-30)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()

        countdown_turtle.write(
            arg=f"Timer: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time-1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(
            arg="Game Over!", move=False, align="center", font=FONT)


def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)


start_game_up()
turtle.mainloop()
