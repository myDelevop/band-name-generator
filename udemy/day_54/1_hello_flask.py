from flask import Flask
app = Flask(__name__)


# We need to sent env variable and run flask run from Terminal (see 2_hello)
@app.route('/')
def hello_world():
    return "Hello, World!"
