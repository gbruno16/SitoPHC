from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    argomento="Ciao"
    data="dat"
    return render_template('index.html',posts=[argomento,data])