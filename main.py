from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the race? Enter a color.")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions=[-70, -40, -10, 20, 50, 80]
all_turtles=[]

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(-230, y=y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 13)
        turtle.forward(rand_distance)
        if turtle.xcor() > 220: 
            is_race_on = False
            winner = turtle.color()[1]

if winner == user_bet:
    print(f"You won the bet! {winner} won")
else:
    print(f"You lost the bet! {winner} won.")

screen.exitonclick()