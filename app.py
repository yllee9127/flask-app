# Simple web application using Flask framework
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Yoon Long!</p>"

@app.route("/happy")
def happy_world():
    return "<p>Happy !</p>"

@app.route("/sad")
def sad_world():
    return "<p>Sad !</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
