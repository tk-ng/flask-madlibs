from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)


@app.route("/")
def home_page():
    words = story.prompts
    return render_template("home.html", words=words)


@app.route("/story")
def show_story():
    place = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adjective = request.args.get("adjective")
    plural_noun = request.args.get("plural_noun")
    return render_template("story.html", place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)
