import turtle
import pandas

import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")

# same as image size or slightly larger
screen.setup(width=850, height=950, startx=50, starty=50)
screen.bgpic("Outline-Map-of-India-with-States.gif")



states = pandas.read_csv("50_states.csv")

score = 0
lives = 5
guessed_states = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title = "guess the state", prompt = f"you have guessed {score} state \nLives left {lives}").title()
    if lives < 1:
        for state in states.state:
            if state not in guessed_states:
                x = states[states.state == state]
                p = turtle.Turtle()
                p.hideturtle()
                p.penup()
                p.goto(int(x.x), int(x.y))
                p.write(state, font=("Arial", 8, "normal"))
        l = turtle.Turtle()
        l.hideturtle()
        l.penup()
        l.goto(0, 0)
        l.write("Game Over!", align="center", font=("courier", 24, "bold"))
        break

    if answer_state in states.state.values:
        x = states[states.state == answer_state]
        guessed_states.append(answer_state)
        score = len(guessed_states)
        p = turtle.Turtle()
        p.hideturtle()
        p.penup()
        p.goto(x=int(x.x.item()), y=int(x.y.item()))
        p.write(answer_state)

    elif answer_state == "Exit":
        missing_states = [state for state in states.state if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(f"The missing states are {missing_states}")
        break

    else:
        lives -= 1
screen.exitonclick()

