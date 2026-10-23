from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'