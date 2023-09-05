import pandas
import turtle


def get_mouse_click_corner(x, y):
    turtle.pu()
    turtle.speed(1)
    turtle.goto(x, y)


def insert_state_in_map(usa_state, position):
    write = turtle.Turtle()
    write.color("black")
    write.penup()
    write.hideturtle()
    write.goto(position)
    write.write(f"{usa_state}", align="center", font=("Courier", 9, "bold"))


states_csv = pandas.read_csv("50_states.csv")
states_dict = states_csv.to_dict(orient='split')

states = []

for state in states_dict["data"]:
    if state != "index":
        states.append({
            "State": state[0],
            "position": (state[1], state[2])
        })

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
screen.setup(width=800, height=600, startx=-260, starty=20)

turtle.onscreenclick(get_mouse_click_corner)

guessed = []

while len(guessed) < 50:
    if len(guessed) > 0:
        textinput = screen.textinput(title=f"{len(guessed)}/{50} States Correct", prompt="What's another state name?")
    else:
        textinput = screen.textinput(title="Guess the State", prompt="What's another state name?")
    if textinput.lower() == "exit":
        break
    check = next((item for item in states if str(item["State"]).lower() == textinput.lower()), None)
    if check is not None and check["State"].lower() not in guessed:
        guessed.append(str(check["State"]).lower())
        insert_state_in_map(check["State"], check["position"])
        get_mouse_click_corner(check["position"][0], check["position"][1])

# The game is finished, we generate a file with the not guessed Countries
with open("states_to_learn.csv", "w") as missed_csv:
    missed_csv.write("state,x,y\n")
    for obj in states:
        if str(obj["State"]).lower() not in guessed:
            missed_csv.write(f"{obj['State']}, {obj['position'][0]}, {obj['position'][1]}\n")

# turtle.mainloop()

