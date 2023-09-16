import random
from flask import Flask, redirect


app = Flask(__name__)
random_num = random.randint(0, 9)
print(random_num)


# We need to sent env variable and run flask run from Terminal (see 2_hello)
@app.route('/')
def hello_world():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


@app.route("/<int:number>")
def guess_number(number):
    if number < 0 or number > 9:
        return redirect("/", code=302)
    else:
        message = ""
        gif_url = ""
        color = ""
        if number > random_num:
            message = "Too high, try again!"
            gif_url = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
            color = "purple"
            print("TOO HIGH")
        elif number < random_num:
            message = "Too low, try again!"
            gif_url = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
            color = "red"
            print("TOO LOW")
        elif number == random_num:
            message = "You found me!"
            gif_url = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
            color = "green"
            print("CONGRATS")

        html = f"<h1 style='color:{color}'>{message}</h1><img src='{gif_url}' width='280'>"

    return html


if __name__ == "__main__":
    # Here we run without terminal and without env variable. If the name of the method
    # is __main__, is a script, then we call app.run() that launches the server directly
    app.run(debug=True)

