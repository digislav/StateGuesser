import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

BACKGROUND = "blank_states_img.gif"
screen.addshape(BACKGROUND)
turtle.shape(BACKGROUND)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
correct_guesses = []

while len(correct_guesses) < 50:
    guess = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another states name?").title()

    if guess in states:
        correct_guesses.append(guess)
        text_overlay = turtle.Turtle()
        text_overlay.hideturtle()
        text_overlay.penup()
        state_data = data[data.state == guess]
        coordinates = (int(state_data.x), int(state_data.y))
        text_overlay.goto(coordinates)
        text_overlay.write(guess)
    elif guess == "Exit":
        missed_states = [state for state in states if state not in correct_guesses]

        df = pandas.DataFrame(missed_states)
        df.to_csv("states_to_learn.csv")

        break

screen.exitonclick()
