from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)


@app.route("/")
def home_page():
    words = story.prompts
    return render_template("home.html", words=words)


@app.route("/story")
def show_story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)
