from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('<h1 style="text-align:center">Hello, World!</h1><p>This is a paragraph</p>'
            '<img width="450" src="https://media.giphy.com/media/X3Yj4XXXieKYM/giphy.gif">')


if __name__ == "__main__":
    app.run(debug=True)
