from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)

app.secret_key = "Welcome Learner"

CARDS = [
    {"question": "What loop structure is used to iterate over an unknown number of items?", "answer": "while loop"},
    {"question": "How many times will the following loop execute? for i in range(5): print(i)", "answer": "5"},
    {"question": "Which data structure is used to store key-value pairs?", "answer": "Dictionary"}
]

@app.route('/', methods=["GET", "POST"])
def hello():

    maxCards = len(CARDS)

    if "lives" not in session:
        session["card_index"] = 0
        session["lives"] = 3

    if request.method == "POST":
        userAnswer = request.form.get("answer").strip().lower()
        if userAnswer == CARDS[session["card_index"]]["answer"].lower().strip():
            session["card_index"] += 1
        else:
            session["lives"] -= 1

    if session["card_index"] >= maxCards:
        return render_template('win.html')
    if session["lives"] <= 0:
        return render_template('lose.html')

    return render_template('index.html', card=CARDS[session["card_index"]], lives=session["lives"])

@app.route('/restart', methods=["GET", "POST"])
def restart():
    ## clears the sessioon to start a new game
    session.clear()
    return redirect('/')