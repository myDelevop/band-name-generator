from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    # Here we run without terminal and without env variable. If the name of the method
    # is __main__, is a script, then we call app.run() that launches the server directly
    app.run()
