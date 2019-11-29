from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    return render_template("index.j2", posts=posts)

