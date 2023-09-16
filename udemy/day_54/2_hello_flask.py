from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!"


# go to http://127.0.0.1:5000/bye
@app.route('/bye')
def say_bye():
    return "Bye"


if __name__ == "__main__":
    # Here we run without terminal and without env variable. If the name of the method
    # is __main__, is a script, then we call app.run() that launches the server directly
    app.run()
