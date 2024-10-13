import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



states = pandas.read_csv("50_states.csv")
list_of_states = states.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another's state name?").title()
    print(answer_state)
    
    if answer_state == "Exit":
        missing_states = [state for state in list_of_states if state not in guessed_states]
        #for state in list_of_states:
        #    if state not in guessed_states:
        #        missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in list_of_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data = states[states.state == answer_state]
        t.goto(data.x.item(),data.y.item())
        t.write(answer_state)
    

screen.exitonclick()