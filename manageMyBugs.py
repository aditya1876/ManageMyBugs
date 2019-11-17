from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    name = request.args.get("name", "World")
    return f'<h1>Hello, {escape(name)}!</h1>'

@app.route('/about')
def about():
    name1 = request.args.get("name", "Earth")
    return f'<h1>I am in about page...i am now {name1}, {escape(name1)}</h1>'