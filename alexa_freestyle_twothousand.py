import logging

from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

from model import *


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def freestyle():
    with open('generated_lyrics/2000-2009Gen.txt', 'r') as generated:
        rap = generated.read().replace('\n', ' ')
    print(rap)
    return statement(rap)

@ask.intent("UselessIntent")
def tester():
	text = "Tester statement."
	return statement(text)


if __name__ == '__main__':
    app.run(debug=True)
