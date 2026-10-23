from flask import Flask, render_template, request, redirect

app = Flask(__name__)

CARDS = [
    {"question": "What loop structure is used to iterate over an unknown number of items?", "answer": "while loop"},
    {"question": "How many times will the following loop execute? for i in range(5): print(i)", "answer": "5"},
    {"question": "Which data structure is used to store key-value pairs?", "answer": "Dictionary"}
]

@app.route('/')
def hello():
    return render_template('index.html', cards=CARDS)