from flask import Flask, render_template, session, request, redirect
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///flashcards.db")

app.secret_key = "Welcome Learner"

@app.route('/', methods=["GET", "POST"])
def hello():

    cards = db.execute('SELECT question, answer FROM cards')
    maxCards = len(cards)

    if "lives" not in session:
        session["card_index"] = 0
        session["lives"] = 3

    if request.method == "POST":
        userAnswer = request.form.get("answer").strip().lower()
        if userAnswer == cards[session["card_index"]]["answer"].lower().strip():
            session["card_index"] += 1
        else:
            session["lives"] -= 1

    if session["card_index"] >= maxCards:
        return render_template('win.html')
    if session["lives"] <= 0:
        return render_template('lose.html')

    return render_template('index.html', card=cards[session["card_index"]], lives=session["lives"])

@app.route('/restart', methods=["GET", "POST"])
def restart():
    ## clears the sessioon to start a new game
    session.clear()
    return redirect('/')