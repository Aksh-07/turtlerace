
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet.", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_positions = [-120, -80, -40, 0, 40, 80, 120]
all_turtles = []
i = 0
for turtle_index in range(6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.setx(-230)
    y = y_positions[i]
    new_turtle.sety(y)
    new_turtle.color(colors[i])
    i += 1
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() < 230:
            rand_dis = random.randint(0, 10)
            turtles.fd(rand_dis)
        else:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"{winning_color} win, Congrats.")
            else:
                print(f"{winning_color} wins, you loose.")

screen.exitonclick()
