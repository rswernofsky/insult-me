import random
from flask import Flask
from flask_cors import CORS


insults = [
    "If brains were dynamite, you wouldn't have enough to blow your nose.",
    "You're not the brightest crayon in the box, are you?",
    "You're a few fries short of a Happy Meal.",
    "Your elevator doesn't quite reach the top floor.",
    "You're not the sharpest tool in the shed.",
    "If stupidity were a talent, you'd be a prodigy.",
    "You're not playing with a full deck, are you?",
    "You're as useful as a screen door on a submarine.",
    "If you had a dollar for every brain cell, you'd be in debt.",
    "You're like a dictionary... except you only have the cover.",
]

app = Flask(__name__)
CORS(app, resources={'/*': {'origins': 'localhost:3000'}})

@app.route("/insult")
def get_insult():
    return random.choice(insults)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
