from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello(name):
    return f"Hello, {escape(name)}!"